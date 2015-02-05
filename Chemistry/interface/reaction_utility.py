# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Middle layer for communication between any interface and the necessary tools
to perform reactions.
"""

__author__ = "Dan Obermiller"


from collections import namedtuple

import networkx as nx

from Chemistry.reactions._reactions import Conditions
from Chemistry.exceptions.ReactionErrors import ReactionError, NoReactionError


def separate_molecules(atoms, bonds):
    """Breaks apart separate molecules into individual objects.

    Parameters
    ----------
    atoms : dict
        Dictionary containing all of the atom keys and their associated
        information.
    bonds : dict
        Dictionary containing all of the bond keys and their associated
        information.

    Returns
    -------
    molecules : list
        A list of dictionaries that can each be easily turned into a Compound.

    Notes
    -----
    The format for the dictionaries is the same as would be provided to the
    Compound constructor, which is documented there.
    The primary point of this is to interface well with a GUI.  Instead of
    trying to have it continually reset and determine whether or not
    """

    molecules = []
    graphs = _get_separate_graphs(atoms, bonds)

    for graph in graphs:
        molecules.append(_graph_to_dict(graph))

    return molecules


def _get_separate_graphs(nodes, edges):
    """Builds the individual graphs from the mega graph.

    Parameters
    ----------
    nodes : dict
        The graph's nodes.
    edges : dict
        The graph's edges.

    Returns
    -------
    graphs : list
        List of the connected subgraphs.
    """

    graphs = []

    big_graph = nx.Graph()

    for key, atom in nodes.iteritems():
        big_graph.add_node(key, {'symbol': atom})

    for key, (first, second, info) in edges.iteritems():
        info.update({'key': key})
        big_graph.add_edge(first, second, info)

    for graph in nx.connected_component_subgraphs(big_graph):
        graphs.append(graph)

    return graphs


def _graph_to_dict(graph):
    """Takes a graph and turns it into valid dictionaries to make a Compound.

    Parameters
    ----------
    graph : networkx.Graph
        The graph being turned into a dictionary.

    Returns
    -------
    molecule : dict
        The dictionary built from the graph.
    """

    molecule = {'atoms': {}, 'bonds': {}}

    for key, atom in graph.node.iteritems():
        molecule['atoms'][key] = atom['symbol']

    for first, rest in graph.edge.iteritems():
        for second, data in rest.iteritems():
            if 'key' in data:
                key = data.pop('key')
                if first < second:
                    molecule['bonds'][key] = first, second, data
                else:
                    molecule['bonds'][key] = second, first, data

    return molecule


def add_other_to_molecule(molecule, info):
    """Adds any necessary additional info to a molecule.

    Parameters
    ----------
    molecule : dict
        A dictionary holding molecular information
    info : dict
        The additional information.
    """

    if 'other_info' in molecule:
        molecule['other_info'].update(info)
    else:
        molecule['other_info'] = info


def build_reaction_conditions(molecules, solvent, **kwargs):
    """Generates a Conditions object based on various factors.

    Parameters
    ----------
    molecules : list
        A list of molecules present in the reaction.  Each of these should
        already have pertinent information, if possible.
    solvent : Solvent
        The solvent in the reaction.  Should have information such as type of
        solvent, pka, concentration, etc.

    Returns
    -------
    cond : Conditions
        The reaction conditions.
    """

    cond_dict = {'molecules': molecules, 'solvent': solvent}
    cond_dict.update(kwargs)
    cond = Conditions(cond_dict)
    return cond


def _handle_acid_base(conditions):
    """Does all of the work necessary to begin an acid base reaction.

    Parameters
    ----------
    conditions : Conditions
        The reaction conditions, including the molecules involved.

    Returns
    -------
    reaction : AcidBase
        The AcidBase reaction object that hass all of the information necessary
        to perform the reaction.
    """

    raise NotImplementedError


supported_reactions = {'acid_base': _handle_acid_base}


def test_reaction(reaction_type, conditions):
    """Tests if a reaction goes to completion, and determines what products it
    generates.

    Parameters
    ----------
    reaction_type : string
        The name of the reaction being attempted
    conditions : Conditions
        The reaction conditions.  Includes a list of the molecules within the
        reaction.

    Returns
    -------
    None, Products, EquilibriumProducts
        Returns the result of the reaction.  If the reaction wouldn't occur then
        None is returned.
    """

    try:
        reaction = supported_reactions[reaction_type](conditions)
    except KeyError:
        raise ReactionError("{} is not a supported reaction")
    else:
        try:
            products = reaction.react()
        except NoReactionError:
            return
        else:
            return products


def pick_best_reaction(reaction_results):
    """Determines the best reaction from a number of attempted reactions.

    Parameters
    ----------
    reaction_results : dict
        A dictionary that maps from reaction type to the result of the reaction.

    Returns
    -------
    best_result : tuple
        A 2-item tuple.  The first item is the type of reaction, and the second
        is the result of the reaction.
    """

    successful_reactions = {name: result
                            for name, result in reaction_results.iteritems()
                            if result}

    Result = namedtuple(
        'Result', ['name', 'result', 'percent_forward', 'time'])

    current_best = Result('', None, 0.0, float('inf'))

    for rxn_name, rxn_result in successful_reactions.iteritems():
        current_result = Result(
            rxn_name, rxn_result, rxn_result.percentage, rxn_result.time)

        current_best = _determine_best(current_best, current_result)

    best_result = current_best.name, current_best.result
    return best_result


def _determine_best(current_best, current_result):
    """Determines the better of two reaction results.

    Parameters
    ----------
    current_best : Result (namedtuple)
        The current best reaction result.
    current_result : Result (namedtuple)
        The reaction result being compared.

    Returns
    -------
    Result (namedtuple)
        The better of the two reaction results.
    """

    better_percentage = (
        current_best.percent_forward > current_result.percent_forward)
    better_time = current_best.time < current_result.time

    # This seems very inefficient and bad right now, but its waiting on a better
    # implementation of the thermodynamic effects of certain reactions.  I'm
    # pretty sure all of this best reaction stuff will eventually move into a
    # preprocessing sort of thing; usually you can predict the type of reaction
    # without actually working out each reaction and then comparing.
    if better_percentage and better_time:
        return current_best
    elif better_percentage:
        return current_best
    elif better_time:
        return current_best
    else:
        return current_result

