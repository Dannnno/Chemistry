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


class Atom(object):
    """An atom.

    Parameters
    ----------
    symbol : string
        The atomic symbol of the atom.
    chirality : string, optional
        The chirality of the atom {'R', 'S'}.
    """

    def __init__(self, symbol, chirality=None, **kwargs):
        self.symbol = symbol
        self.lpe = 0
        self.chirality = chirality

    # This prevents us from actually making copies of any atomic data.  All data
    # not inherent to this specific Atom instance will be pulled from the
    # existing periodic table
    def __getattr__(self, attr):
        return pt[self.symbol][attr]

    def add_lone_pair(self, n=1):
        """Adds `n` lone pair electrons to the atom.

        Parameters
        ----------
        n : int, optional
            The number of lone pairs of electrons to add to the atom.

        Raises
        ------
        ValueError
            Thrown if too many lone pairs are added (would violate the octet
            rule for the atomic center).
        """

        # TODO: Create a working implementation of formal charge and how to
        #       interpret the octet rule
        raise NotImplementedError


class Bond(object):
    """A bond between two atoms.

    Parameters
    ----------
    first, last : Atom
        Adjacent nodes (atoms) to the edge (bond).  Order doesn't matter.
    order : int, optional
        The order of the

    """

    _atoms = None
    _order = 1

    def __init__(self, first, last, order=1, **kwargs):
        self.atoms = {first, last}
        self.order = order
        for key, arg in kwargs.iteritems():
            if not hasattr(self, key):
                self.__dict__[key] = arg

    @property
    def atoms(self):
        return self._atoms

    @atoms.setter
    def atoms(self, atoms):
        self._atoms = atoms

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, ord_):
        ord_ = int(ord_)
        if ord_ not in {1, 2, 3}:
            raise ValueError(
                "A bond can only have order 1, 2, or 3, not {}".format(ord_))
        else:
            self._order = ord_

    def __iter__(self):
        yield self.atoms


# Everything past this is unimplemented, and should not be taken as a guarantee
# that they will be implemented.


class Electron(object):

    def __init__(self):
        raise NotImplementedError


class Proton(object):

    def __init_(self):
        raise NotImplementedError


class Neutron(object):

    def __init__(self):
        raise NotImplementedError


class Orbital(object):

    def __init__(self):
        raise NotImplementedError


class SOrbital(Orbital):

    def __init__(self):
        super(SOrbital, self).__init__()


class POrbital(Orbital):

    def __init__(self):
        super(SOrbital, self).__init__()


# D and F orbitals are not relevant at this time.
