# Copyright (c) 2014 Dan Obermiller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# You should have received a copy of the MIT License along with this program.
# If not, see <http://opensource.org/licenses/MIT>


"""Middle layer for communication between any interface and the necessary tools
to perform reactions.
"""


import networkx as nx

# from Chemistry.interface.compound_utility import compound_from_dict
# from Chemistry.base.periodic_table import get_element


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
        molecule['atoms'][key] = atom

    for first, rest in graph.edge.iteritems():
        for second, data in rest.iteritems():
            key = data.pop('key')
            molecule['bonds'][key] = first, second, data

    return molecule

        # self.get_information()
        # self.to_compound()
        # self.generate_conditions()
        # self.list_reactions()
        # self.test_reactions()
        # self.pick_result()
        # self.build_instructions()
        # self.display_result()

separate_molecules({'a1': 'H', 'a2': 'H', 'a3': 'H'},
    {'b1': ('a1', 'a2', {'order': 1, 'chirality': None})})