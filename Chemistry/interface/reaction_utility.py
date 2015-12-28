# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Middle layer for communication between any interface and the necessary tools
to perform reactions.

I would expect that the general process of a reaction should be as follows:

1. Build the molecules
    Often they'll all be in one big dictionary, so separate_molecules should be
    used to break them up.  Then any additional information should be added to
    them (this will generally not happen, unless file parsing is involved
    or the interface specifically adds this information.  Lastly, they should be
    converted to actual Compound objects.
2. Build the reaction conditions
    This means we need sufficient information to determine which reaction is
    most likely.
3. Predict the reaction
4. Conduct the reaction
    If the reaction is successful, goto [5].  Otherwise go back to [3] and try
    another reaction.n
5. Return the result.
"""

__author__ = "Dan Obermiller"


import networkx as nx

from Chemistry.reactions._reactions import Conditions
from Chemistry.exceptions.ReactionErrors import ReactionError, NoReactionError  # noqa


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
