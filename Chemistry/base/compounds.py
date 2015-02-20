# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository


"""This module provides the underlying framework for the package. It provides
the base Compound class that is used throughout to represent molecules, as well
as the abstract class _CompoundWrapper that is used throughout whenever the
Compound class is wrapped (such as by Reactant).  These classes are fundamental
to the rest of the program.
"""

__author__ = "Dan Obermiller"


import abc
import json

import networkx as nx

from Chemistry.base.components import Atom, Bond


class Compound(nx.Graph):
    """A molecule stored in all its glory.

    Implemented as a graph (subclassing networkx.Graph).

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
    atoms
    bonds
    other_info
    charge
    """

    _atoms = None
    _bonds = None
    _other = None
    resonance_structures = None

    @staticmethod
    def _node_matcher(node1, node2):
        """Helper function to check for isomorphic graphs.

        Parameters
        ----------
        node1 : Object
            The first node evaluated when checking graph isomorphism.
        node2 : Object
            The second node evaluated when checking graph isomorphism.

        Returns
        -------
        bool
            Whether or not the nodes can be considered equivalent.
        """

        return node1['symbol'] == node2['symbol']

    @staticmethod
    def _edge_matcher(edge1, edge2):
        """Helper function to check for isomorphic graphs.

        Parameters
        ----------
        edge1 : Object
            The first edge evaluated when checking graph isomorphism.
        edge2 : Object
            The second edge evaluated when checking graph isomorphism.
        """

        return edge1 == edge2

    def __init__(self, atoms, bonds, other_info=None):
        super(Compound, self).__init__()
        if other_info is None:
            other_info = {}
        self.atoms = atoms
        self.bonds = bonds
        self.other_info = other_info
        self.molecule = {'other_info': self.other_info,
                         'atoms': self.atoms,
                         'bonds': self.bonds}
        self.auto_complete()
        self.get_resonance_structures()

    @property
    def atoms(self):
        """The atoms of a molecule.

        Returns
        -------
        self._atoms : dict
            The dictionary that stores all of the atoms in a molecules.
        """

        return self._atoms

    @atoms.setter
    def atoms(self, nodes):
        if self._atoms is None:
            self._atoms = {}
        self._add_nodes_from(nodes)

    @property
    def bonds(self):
        """The bonds of a molecule.

        Returns
        -------
        self._bonds : dict
            The dictionary that stores all of the bonds in a molecules.
        """

        return self._bonds

    @bonds.setter
    def bonds(self, edges):
        if self._bonds is None:
            self._bonds = {}
        self._add_edges_from(edges)

    @property
    def other_info(self):
        """Other information about a molecule.

        Returns
        -------
        self._other : dict
            The dictionary that stores all other information in a molecule.
        """

        return self._other

    @other_info.setter
    def other_info(self, info):
        self._other = info
        self.graph.update(self._other)

    def _add_nodes_from(self, atoms):
        """Adds a group of nodes.

        Parameters
        ----------
        atoms : dict
            The atoms that are being added to the molecule.
        """

        for key, atom in atoms.iteritems():
            self._add_node(key, Atom(atom))

    @property
    def charge(self):
        """The charge of a molecule.

        Returns
        -------
        charge : int
            The net charge on a molecule.
        """

        charge = sum(atom.charge for atom in self.atoms.itervalues())
        return charge

    def _add_edges_from(self, bonds):
        """Adds a group of edges.

        Parameters
        ----------
        bonds : dict
            The bonds that are being added to the molecule.
        """

        for id_, bond in bonds.iteritems():
            self._add_edge(id_, *bond)

    def _add_node(self, key, atom):
        """Adds a single node.

        Parameters
        ----------
        key : string
            The key associated with the given atom.
        atom : Atom
            An atom object.
        """

        if key in self.atoms:
            raise KeyError("There is already an atom {}".format(key))
        self.add_node(key, {'symbol': atom.symbol})
        self.atoms[key] = atom

    def _add_edge(self, key, first, second, rest=None):
        """Adds a single edge.

        Parameters
        ----------
        key : string
            The key associated with the given atom.
        first : string
            The key of one of the atoms in the bond
        second : string
            The key of the other atom in the bond
        rest : dict, optional
            Other information relevant to the bond.
        """

        if rest is None:
            rest = {}
        if key in self.bonds:
            raise KeyError("There is already a bond {}".format(key))
        else:
            bond = Bond(self.atoms[first], self.atoms[second], **rest)
            self.add_edge(first, second, key=key, bond_obj=bond)
            self.bonds[key] = bond

    def auto_complete(self):
        """Fills up the atom with necessary hydrogens and lone pairs.

        Notes
        -----
        This assumes that all Carbons will have 4 bonds, and empty bonds will
        be to Hydrogens.  It assumes that all other molecules will be filled
        with lone pairs until the octet rule is satisfied.
        """

        pass

    def get_resonance_structures(self):
        """Builds a list of available resonance structures for this compound.

        Notes
        -----
        In general, resonance can be determined by following a number of rules,
        given here in the (approximate) order in which they should be followed.

        1. Octet rule trumps.
            Compounds favor arrangements that conform to the octet rule (except
            for centers that can have expanded octets).  Except for those
            centers, all structures must meet the octet rule.
        2. Separation of formal charge should be avoided.
            While formal charge is inevitable in some cases, it is better to
            have charges closer together.
        3. Formal charge is to be avoided.
            The example structure above has a negative charge on it, located on
            the two Oxygen atoms (or more accurately shared between them).  This
            formal charge is unavoidable, however in other structures there will
            be arrangements that have more (or less) atoms exhibiting formal
            charge.
        4. There must be driving force.
            There must be a reason for the electrons to move.  This all comes
            down to more favorable energy states.
        5. sp3 hybridized atoms are off-limits for resonance
            They don't have the open p-orbital necessary for resonance to occur.
        6. Lone pairs can't jump atoms, but pi-bonds can.
            Lone pair electrons move from bond to atom to bond, while a pi-bond
            can jump to the other side of one of its nodes.
        """

        potential_atoms = [atom for atom in self.atoms.itervalues()
                           if atom.could_resonate()]
        potential_bonds = [bond
                           for bond in self.bonds.itervalues()
                           if bond.could_resonate()]

    def __str__(self):
        return json.dumps(
            self.molecule, cls=_ChemicalSerializer, sort_keys=True)

    def __repr__(self):
        return json.dumps(
            self.molecule, cls=_ChemicalSerializer, sort_keys=True, indent=4)

    def is_isomorphic(self, other):
        """Determines whether or not a molecule is isomorphically equivalent
        to another.

        Parameters
        ----------
        other : Compound, _CompoundWrapper
            The Compound that is being check for isomorphism.

        Returns
        -------
        bool
            Whether or not the molecules are isomorphic.
        """

        return nx.is_isomorphic(self, other,
                                node_match=self._node_matcher,
                                edge_match=self._edge_matcher)

    def __eq__(self, other):
        return self.is_isomorphic(other)

    def __ne__(self, other):
        return not self.is_isomorphic(other)


class _CompoundWrapper(object):
    """Abstract base class for compound wrapping classes.

    Parameters
    ----------
    compound : Compound
        The compound being wrapped.

    Attributes
    ----------
    compound

    Notes
    -----
    This class exists to be sub-classed by other classes, such as Reactant, or
    Product.  This is easier than creating a brand new Compound object whenever
    I want to analyze a molecule as an Acid, or a Base, or some other reactant
    or product.
    """

    __metaclass__ = abc.ABCMeta
    _compound = None

    def __init__(self, compound):
        self.compound = compound

    @property
    def compound(self):
        """The underlying compound object that is being wrapped.

        Returns
        -------
        self._compound : Compound
            The compound object.
        """

        return self._compound

    @compound.setter
    def compound(self, comp):
        self._compound = comp

    def __getattr__(self, attr):
        return getattr(self.compound, attr)

    def __eq__(self, other):
        if hasattr(other, 'compound'):
            return self.compound == other.compound
        else:
            return self.compound == other

    def __str__(self):
        return str(self.compound)

    def __repr__(self):
        return repr(self.compound)

    def __len__(self):
        return len(self.compound)

    def __getitem__(self, key):
        return self.compound[key]


class _ChemicalSerializer(json.JSONEncoder):
    """Encoder class that ensures custom chemistry classes are serializable.
    Will have items added as necessary.
    """

    def default(self, o):
        """Overrides the original implementation of the JSONEncoder.

        Parameters
        ----------
        o : Object
            Any object to be serialized.

        Returns
        -------
        dict
            A dictionary with the post-serialization values of the object.

        Raises
        ------
        TypeError
            Thrown when an object has neither __dict__ nor __slots__ (which as
            far as I can tell are only some of the builtin types) and json
            doesn't have any default support for the type.

        Notes
        -----
        Any custom classes created for this project that are likely to be
        serialized should be added to this method.  Falls back to using the
        object's dictionary, then slots, and then to the original behavior.
        """

        if isinstance(o, Atom):
            return {'symbol': o.symbol}
        elif isinstance(o, Bond):
            return {'members': (o.first, o.second)}
        elif hasattr(o, '__dict__'):
            return o.__dict__
        elif hasattr(o, '__slots__'):
            return {key: getattr(o, key) for key in o.__slots__}
        else:
            return super(_ChemicalSerializer, self).default(o)
