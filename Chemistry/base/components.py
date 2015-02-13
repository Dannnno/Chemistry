# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""The underlying components of chemical compounds.  Includes things such as
atoms and bonds, as well as even lower level things such as protons, neutrons,
electrons, orbitals, etc.  Note that not all of those are necessarily
implemented at this time, or will be implemented, however if/when they are
implemented they would exist here (until such time as this module is further
broken up.
"""

__author__ = "Dan Obermiller"

from Chemistry.base.periodic_table import periodic_table as pt
from Chemistry.exceptions.AtomicErrors import ValenceError


class Atom(object):
    """An atom.

    Parameters
    ----------
    symbol : string
        The atomic symbol of the atom.
    chirality : string, optional
        The chirality of the atom {'R', 'S'}.

    Attributes
    ----------
    charge
    steric_num
    lpe
    num_bonds
    bonds
    hybridization
    available_orbitals
    eneg : float
        The electronegativity of the atom.
    group : int
        The atomic group of the atom.
    melt : float
        The melting point of the atom.
    mass : float
        The atomic mass of the atom.
    density : float
        The atomic density of the atom
    symbol : string
        The atomic symbol of the atom.
    name : string
        The full name of the atom.
    number : int
        the atomic number of the atom.
    boil : float
        The boiling point of the atom.
    radius : float
        The atomic radius of the atom.
    oxidation : list
        A list of possible oxidation states of the atom.
    valence : int
        The valence number of the atom.

    Notes
    -----
    The attributes of `charge`, `steric_num`, `num_bonds`, `hybridization` and
    `available_orbitals` are all calculated values; meaning every time
    AtomInstance.charge is called (for example) the charge will be recalculated.
    Thus it is generally advised to call it once and store that result as
    another variable (if it will be used more than once).
    """

    _lpe = 0
    _bonds = None
    _hybridization_states = {4: 'sp3', 3: 'sp2', 2: 'sp1'}
    _orbitals = {'sp3': ['sp3', 'sp3', 'sp3', 'sp3'],
                 'sp2': ['sp2', 'sp2', 'sp2', 'p'],
                 'sp1': ['sp1', 'sp1', 'p', 'p']}
    _attr_to_keys = {"eneg": "Electronegativity",
                     "group": "Group",
                     "melt": "Melting Point",
                     "mass": "Weight",
                     "density": "Density",
                     "symbol": "Symbol",
                     "name": "Element",
                     "number": "Atomic Number",
                     "boil": "Boiling Point",
                     "valence": "Valence",
                     "radius": "Atomic Radius",
                     "oxidation": "Oxidation Number(s)"
                    }

    def __init__(self, symbol, chirality=None, **kwargs):
        self._bonds = []
        self.symbol = symbol
        self.chirality = chirality

    # This prevents us from actually making copies of any atomic data.  All data
    # not inherent to this specific Atom instance will be pulled from the
    # existing periodic table
    def __getattr__(self, attr):
        if attr == '__deepcopy__':
            return super(Atom, self).__deepcopy__
        # This actually doesn't work right now.  The attributes detailed above
        # are not properly retrieved, see open issue #30
        try:
            return pt[self.symbol][self._attr_to_keys[attr]]
        except KeyError:
            raise AttributeError("Atom object has no attribute {}".format(attr))

    @property
    def charge(self):
        """The formal charge of the molecule.

        Notes
        -----
        Formal charge is calculated as valence - lpe - shared/2.  That is, the
        number of valence electrons minus the number of lone pair electrons
        minus half the number of shared electrons (ie the sum of bond orders).
        """

        return self.valence - self.lpe - self._get_shared()

    def _get_shared(self):
        """Determines how many shared electrons an atom has.

        Returns
        -------
        int
            The number of shared electrons.

        Notes
        -----
        This is functionally equivalent to the sum of the order of the bonds).
        """

        return sum(bond.order for bond in self.bonds)

    @property
    def steric_num(self):
        """The steric number of the atom.

        Notes
        -----
        Used in determining hybridization. Steric number is calculated as no. of
        atoms bonded to plus the number of lone pair electrons.
        """

        return self.num_bonds + self.lpe

    # lpe is a read-only property.  It should only be modified by the functions
    # below, which should directly modify the underlying value of _lpe.

    @property
    def lpe(self):
        """The number of lone pair electrons on an atom.

        Returns
        -------
        self._lpe : int
            The number of lone pair electrons.
        """

        return self._lpe

    @property
    def num_bonds(self):
        """The number of bonds this atom has.

        Returns
        -------
        int
            The number of bonds.
        """

        return len(self.bonds)

    @property
    def bonds(self):
        """The bonds this atom has.

        Returns
        -------
        self._bonds : list
            This atom's bonds.
        """

        return self._bonds

    @property
    def hybridization(self):
        """The hybridization of the atom.

        Returns
        -------
        hybrid : string
            The hybridization of the atom.

        References
        ----------
        http://chemistry.stackexchange.com/a/4405/4148
        """

        if self.steric_num in self._hybridization_states:
            return self._hybridization_states[self.steric_num]
        else:
            return "unhybridized"

    @property
    def available_orbitals(self):
        """The available bonding orbitals of an atom.

        Returns
        -------
        list
            A list of available bonding orbitals.
        """

        hybrid = self.hybridization
        if hybrid == "unhybridized":
            # This depends on the atom in question.  I'll need to figure out a
            # good way to determine this.  Maybe just more information in the
            # periodic table?
            raise NotImplementedError
        else:
            return self._orbitals[hybrid]

    def add_bond(self, bond, other=None):
        """Adds a bond to another atom.

        Parameters
        ----------
        bond : Bond
            The bond to the other atom.
        other : Atom
            The atom being bonded to.
        """

        self.bonds.append(bond)
        if other is not None:
            other.add_bond(bond)

    def remove_bond(self, bond, other=None):
        """Removes a bond to another atom.

        Parameters
        ----------
        bond : Bond
            The bond being broken
        other : Atom
            The atom on the other end of the bond.
        """

        self.bonds.remove(bond)
        if other is not None:
            other.remove_bond(bond)

    def add_lone_pair(self, n=1):
        """Adds `n` lone pair electrons to the atom.

        Parameters
        ----------
        n : int, optional
            The number of lone pairs of electrons to add to the atom.

        Raises
        ------
        ValenceError
            Thrown if too many lone pairs are added (would violate the octet
            rule for the atomic center).
        """

        # TODO: Create a working implementation of formal charge and how to
        #       interpret the octet rule

        raise NotImplementedError

    def remove_lone_pair(self, n=1):
        """Removes `n` lone pair electrons from the atom.

        Parameters
        ----------
        n : int, optional
            The number of lone pairs to remove.

        Raises
        ------
        ValenceError
            Thrown if too many lone pairs would be removed (ie more than are
            present).
        """

        raise NotImplementedError

    def could_resonate(self):
        """Determines if the atom has the potential to be involved in a
        resonance structure.

        Returns
        -------
        bool
            Whether the atom has the appropriate hybridization.
        """

        return self.hybridization != 'sp3'

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __ne__(self, other):
        return not self == other


class Bond(object):
    """A bond between two atoms.

    Parameters
    ----------
    first, second : Atom
        Adjacent nodes (atoms) to the edge (bond).  Order doesn't matter.
    order : int, optional
        The order of the bond.

    Attributes
    ----------
    atoms
    order
    """

    _atoms = None
    _order = 1

    def __init__(self, first, second, order=1, **kwargs):
        self.first = first
        self.second = second
        self.first.add_bond(self, other=self.second)
        self.atoms = [first, second]
        self.order = order
        for key, arg in kwargs.iteritems():
            if not hasattr(self, key):
                self.__dict__[key] = arg

    @property
    def atoms(self):
        """The atoms in a bond.

        Returns
        -------
        self._atoms : set
            A set (unordered, collection) of the atoms in the bond.
        """

        return self._atoms

    @atoms.setter
    def atoms(self, atoms):
        self._atoms = atoms

    @property
    def order(self):
        """The order of the bond.

        Returns
        -------
        self._order : int
            The order of the bond (1, 2, or 3)

        Raises
        ------
        ValueError
            Thrown whenever an invalid order is assigned (ie values greater than
            3 or values less than 1).  Non-integer values should be avoided but
            they will be rounded using the `int()` function.
        """

        return self._order

    @order.setter
    def order(self, ord_):
        ord_ = int(ord_)
        if ord_ not in {1, 2, 3}:
            raise ValueError(
                "A bond can only have order 1, 2, or 3, not {}".format(ord_))
        else:
            self._order = ord_

    def __getitem__(self, key):
        if key == 0:
            return self.first
        elif key == 1:
            return self.second
        else:
            raise KeyError("Bonds only have two items")

    def could_resonate(self):
        """Determines if this bond could be an active member of a resonance
        structure.

        Returns
        -------
        bool
            Whether or not both of its adjacent atoms are non-sp3 hybridized.
        """

        return all(atom.could_resonate() for atom in self)

    def __iter__(self):
        for atom in self.atoms:
            yield atom
        raise StopIteration

    def __eq__(self, other):
        direct = self.first == other.first and self.second == other.second
        reverse = self.first == other.second and self.second == other.first
        order = self.order == other.order
        return order and (direct or reverse)

    def __ne__(self, other):
        return not self == other


# Everything past this is unimplemented, and should not be taken as a guarantee
# that they will be implemented.


# class Electron(object):
#
#     def __init__(self):
#         raise NotImplementedError
#
#
# class Proton(object):
#
#     def __init__(self):
#         raise NotImplementedError
#
#
# class Neutron(object):
#
#     def __init__(self):
#         raise NotImplementedError
#
#
# class Orbital(object):
#
#     def __init__(self):
#         raise NotImplementedError
#
#
# class SOrbital(Orbital):
#
#     def __init__(self):
#         super(SOrbital, self).__init__()
#
#
# class POrbital(Orbital):
#
#     def __init__(self):
#         super(SOrbital, self).__init__()


# D and F orbitals are not relevant at this time.
