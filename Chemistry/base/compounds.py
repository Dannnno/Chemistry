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

from collections import deque
import json
import types

import networkx as nx

import Chemistry.base.periodic_table as pt


class Compound(nx.Graph):
    """A molecule stored in all its glory.

    Is stored and implemented as a graph (subclassing networkx.Graph).

    Parameters
    ----------
    atoms : dict
        A dictionary storing all the atoms of a molecule.  Should be presented
        in a form like
            `{'a1': 'H', 'a2': 'O', 'a3': 'H'}`.
        Accepted format is "a#" as a key and the atom's atomic symbol as the
        value.
    bonds : dict
        A dictionary storing all the bonds of a molecule.  Should be presented
        in a form like
            `{'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}`.
        Accepted format is "b#" as a key and a three-item tuple as the value.
        The items at indices 0 and 1 should be the keys of the two atoms being
        bonded (order doesn't matter here) and the item at index 2 should be a
        dictionary of relevant information.  Information that is not provided
        will be assigned reasonable default values.  The chirality is from
        index 0 to index 1 of the tuple.
    other_info : dict, optional.
        A dictionary that stores all other relevant information about a
        molecule.  Things like molecular charge, pka, the name/id of the
        molecule, etc.  If no information is provided the constructor will
        attempt to ascertain any information it needs.

    Attributes
    ----------
    filetypes : dict
        A dictionary of supported filetypes.  The key is the filetype, the
        value is a tuple of two functions.  The first is the function that
        generates a Compound object from a file, the second is the function
        that generates a file from the Compound instance it is passed.
    BUILD_COMPOUND : { 0 }
        Constant representing index 0.  Used to specify which method to use
        from the filetype dict
    BUILD_FILE : { 1 }
        Constant representing index 1.  Used to specify which method to use
        from the filetype dict
    """

    @classmethod
    def json_serialize(cls, obj, as_str=False):
        """Serializes an object for json, used for __str__ and __repr__

        Parameters
        ----------
        obj : Object
            The object to be serialized.  Can be anything, although this
            function is largely intended to work with Compound objects
        as_str : bool, optional
            Specifies whether `repr` or `str` will be used to generate the
            strings
        """

        stringify_function = (repr if not as_str else str)
        d = {}
        try:
            if isinstance(obj, Compound):
                for key, value in obj.__dict__.iteritems():
                    if key in ['atoms', 'bonds', 'other_info']:
                        d.update({key: value})
                return d
            else:
                return obj.__dict__
        except AttributeError:
            return map(stringify_function, obj)

    @classmethod
    def node_matcher(cls, node1, node2):
        """Helper function to check for isomorphic graphs

        Parameters
        ----------
        node1 : Object
                The first node evaluated when checking graph isomorphism
        node2 : Object
                The second node evalutated when checking graph isomorphism

        Returns
        -------
        bool
            Whether or not the nodes can be considered equivalent
        """

        return node1['symbol'] == node2['symbol']

    @classmethod
    def edge_matcher(cls, edge1, edge2):
        """Helper function to check for isomorphic graphs

        Parameters
        ----------
        edge1 : Object
                The first edge evaluated when checking graph isomorphism
        edge2 : Object
                The second edge evalutated when checking graph isomorphism
        """

        return edge1 == edge2

    def __init__(self, atoms, bonds, other_info={}):
        super(Compound, self).__init__()
        self.atoms = {}
        self.bonds = {}

        self._add_nodes_from(atoms)
        self._add_edges_from(bonds)
        self.other_info = other_info
        self.graph.update(self.other_info)
        self.molecule = {'other_info': self.other_info,
                         'atoms': self.atoms,
                         'bonds': self.bonds}

    def _add_nodes_from(self, atoms):
        """Adds a group of nodes

        Parameters
        ----------
        atoms : dict
                The atoms that are being added to the molecule
        """

        for key, atom in atoms.iteritems():
            self._add_node(key, pt.get_element(atom))

    def _add_edges_from(self, bonds):
        """Adds a group of edges

        Parameters
        ----------
        bonds : dict
                The bonds that are being added to the molecule
        """

        for id_, bond in bonds.iteritems():
            self._add_edge(id_, *bond)

    def _add_node(self, key, atom):
        """Adds a single node.  Should probably be a property"""

        try:
            _ = self.atoms[key]
        except KeyError:
            self.add_node(key, **atom)
            self.atoms[key] = atom['symbol']
        else:
            raise KeyError("There is already an atom {}".format(key))

    def _add_edge(self, key, first, second, rest={}):
        """Adds a single edge. Should probably be a property"""

        try:
            _ = self.bonds[key]
        except KeyError:
            d = {'order':1, 'chirality':None}
            d.update(rest)
            self.add_edge(first, second, key=key, **d)
            self.bonds[key] = first, second, d
        else:
            raise KeyError("There is already a bond {}".format(key))

    def path(self, atoms, bonds=[]):
        """Locates a path that contains the specified atoms/bonds"""

        if bonds:
            return self._path(atoms, bonds)
        first = self._get_first(atoms[0])
        paths = []
        for start in first:
            temp = self._get_path(start, atoms[1:])
            if temp:
                paths.append(temp)
        return set(self._flatten_tuples(self._get_tuples(paths)))

    def _get_tuples(self, mixed_list):
        """This function is necessary because there appears to be a bug
        in my path-finding algorithm, sometimes I get lists when I don't
        want them.  Once I find and fix that this'll be removed
        """

        tup = deque()
        if isinstance(mixed_list, (list, deque, tuple)):
            for t in mixed_list:
                if t:
                    if isinstance(t, (list, deque)):
                        tup.extendleft(self._get_tuples(t))
                    else:
                        tup.appendleft(t)
        return tup

    def _flatten_tuples(self, tuple_):
        """This function is necessary because I can't figure out why my
        tuples are becoming nested
        """

        if len(tuple_) == 1:
            return tuple(self._flatten_tuples(tuple_[0]))
        else:
            tup = deque()
            for item in tuple_:
                if isinstance(item, tuple):
                    tup.append(self._flatten_tuples(item))
                else:
                    tup.append(item)
            return tuple(tup)

    def _path(self, atoms, bonds):
        """Helper function to find paths"""

        if not all(isinstance(bond, (dict, types.NoneType)) for bond in bonds):
            raise TypeError("All information in bonds must be a NoneType or a dict")
        first = self._get_first(atoms[0])
        paths = []
        for start in first:
            temp = self._get_path_with_bond(start, atoms[1:], bonds)
            if temp:
                paths.append(temp)
        return set(self._flatten_tuples(self._get_tuples(paths)))

    def _get_path(self, starting_point, rest, so_far=()):
        """Helper function to find paths"""

        so_far += (starting_point,)

        next_atom = self._get_next(starting_point, so_far, rest[0])

        if len(rest) == 1:
            return tuple(so_far + (atom,) for atom in next_atom)
        else:
            ret_tuples = map(lambda x:
                                self._get_path(
                                    x, rest[1:], so_far),
                             next_atom)
            return ret_tuples

    def _get_path_with_bond(self, starting_point, rest, bonds, so_far=()):
        """Helper function to find paths"""

        so_far += (starting_point,)

        next_atom = self._get_next_with_bond(
                            starting_point, so_far, bonds[0], rest[0])

        if len(rest) == 1:
            return tuple(so_far + (atom,) for atom in next_atom)
        else:
            ret_tuples = map(lambda x:
                                self._get_path_with_bond(
                                    x, rest[1:], bonds[1:], so_far),
                             next_atom)
            return ret_tuples

    def _join_paths(self, first, second):
        """Cleanly combines two path sections"""

        if first:
            if first[-1] == second[0]:
                return first[:-1] + second
            else:
                return first + second
        else:
            return second

    def _get_first(self, atom):
        """Helper function to find paths"""

        return [key
                 for key, value in self.atoms.iteritems()
                 if value == atom]

    def _get_next(self, atom, visited, next_=None):
        """Helper function to find paths"""

        return self._filter_next(self._next_(atom), visited, next_=next_)

    def _get_next_with_bond(self, atom, visited, bond, next_=None):
        """Helper function to find paths"""

        if bond is None:
            return self._get_next(atom, visited, next_)
        else:
            possible_neighbors = self._filter_next(self._next_(atom),
                                                   visited,
                                                   next_)
            valid_neighbors = ()
            for neighbor in possible_neighbors:
                info = self.edge[atom][neighbor].items()
                if all(data in info for data in bond.iteritems()):
                    valid_neighbors += (neighbor,)
            return valid_neighbors

    def _next_(self, atom):
        """Helper function to find paths"""

        try:
            return self.neighbors(atom)
        except nx.exception.NetworkXError:
            raise KeyError("{} not in the graph".format(atom))

    def _filter_next(self, neighbors, visited, next_=None):
        """Helper function to find paths"""

        return tuple(neighbor
                      for neighbor in neighbors
                      if neighbor not in visited and
                         ((next_ is not None and
                           self.atoms[neighbor] == next_) or
                          (next_ is None)))

    def __str__(self):
        return json.dumps(Compound.json_serialize(self, as_str=True),
                           sort_keys=True,
                           indent=4)

    def __repr__(self):
        return json.dumps(Compound.json_serialize(self),
                           sort_keys=True,
                           indent=4)

    def is_isomorphic(self, other):
        """"""

        return nx.is_isomorphic(self, other,
                                node_match=Compound.node_matcher,
                                edge_match=Compound.edge_matcher)

    def __eq__(self, other):
        return self.is_isomorphic(other)

    def __ne__(self, other):
        return not self.is_isomorphic(other)
