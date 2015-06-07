# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository


"""This module provides the classes used to form various reactants in a
chemical reaction.
"""

__author__ = "Dan Obermiller"


from copy import deepcopy

from .components import Atom
from .compounds import _CompoundWrapper


class Reactant(_CompoundWrapper):
    """The base Reactant object.  All subclasses of this are things that
    are commonly found in a reaction.

    Parameters
    ----------
    compound : Compound
        The molecule being considered as a reactant.

    Attributes
    ----------
    pka
    """

    _pka = None

    @staticmethod
    def _new_key(compound, atom=True):
        """Generates a new atom/bond key for a compound.

        Parameters
        ----------
        compound : Compound, _CompoundWrapper
            The compound that needs a new key
        atom : bool, optional
            True if a new atom key is needed, False for new bond key.  Defaults
            to True.

        Returns
        -------
        string
            The new key.
        """

        if atom:
            max_key = max(compound.atoms)
            letter = 'a'
        else:
            max_key = max(compound.bonds)
            letter = 'b'
        number = int(max_key[1:]) + 1
        return "{}{}".format(letter, number)

    def __init__(self, compound):
        super(Reactant, self).__init__(compound)

    @property
    def pka(self):
        """The pka of a molecule.  If the wrapped molecule already has a known
        pka then the value passed by the constructor is checked against that.
        """

        return self._pka

    @pka.setter
    def pka(self, pka_):

        if hasattr(self.compound, 'pka'):
            if pka_ != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))

        self._pka = pka_

    def __str__(self):
        return "{} of {}".format(
            self.__class__.__name__, self.compound.__class__.__name__
        )

    def __repr__(self):
        return str(self)


class Acid(Reactant):
    """A subclass of Reactant, represents acidic compounds in a reaction.

    Parameters
    ----------
    compound : Compound
        The molecule being treated as an acid.
    acidic_point : string
        The key of the 'acidic point' of the molecule, or the most acidic H+.
    pka : float
        The pKa of the aforementioned most acidic H+.
    """

    def __init__(self, compound, acidic_point, pka):
        super(Acid, self).__init__(compound)
        self.acidic_point = acidic_point
        self.pka = pka

    def to_conjugate_base(self):
        """Transforms the current acid into its conjugate base."""

        raise NotImplementedError


class Base(Reactant):
    """A subclass of Reactant, represents basic compounds in a reaction.

    Parameters
    ----------
    compound : Compound
        The molecule being treated as a base.
    basic_point : string
        The key of the 'basic point' of the molecule, or the location that is
        most accepting of H+.
    pka : float
        The pKa of the conjugate acid.
    """

    def __init__(self, compound, basic_point, pka):
        super(Base, self).__init__(compound)
        self.basic_point = basic_point
        self.pka = pka

    def to_conjugate_acid(self):
        """Transforms the current base into its conjugate acid.  Is side-effect
        free; all changes happen on a copy of this base.

        Returns
        -------
        Acid
            The conjugate acid of the base."""

        conjugate = deepcopy(self.compound)
        a_key = Reactant._new_key(conjugate)
        b_key = Reactant._new_key(conjugate, False)
        hydrogen = Atom('H')
        conjugate._add_node(a_key, hydrogen)
        conjugate._add_edge(b_key, a_key, self.basic_point)
        try:
            conjugate.other_info['id'] = "Conjugate acid of {}".format(
                self.other_info['id']
            )
        except KeyError:
            conjugate.other_info['id'] = "Unknown acid"
        return Acid(conjugate, a_key, self.pka)


class LewisAcid(Acid):
    pass


class LewisBase(Base):
    pass


class BronstedAcid(Acid):
    pass


class BronstedBase(Base):
    pass


class Electrophile(Reactant):
    pass


class Nucleophile(Reactant):
    pass
