# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""This module provides the tools to simulate an acid base reaction."""

__author__ = "Dan Obermiller"


from copy import deepcopy

from Chemistry.base import compounds
from Chemistry.reactions._reactions import _Reaction, Conditions
from Chemistry.base.products import Product, Products, EquilibriumProducts
from Chemistry.exceptions.ReactionErrors import NoReactionError


class AcidBase(_Reaction):
    """Performs an acid base reaction.

    Parameters
    ----------
    acid : Acid
        The acid in the reaction.
    base : Base
        The base in the reaction.
    cond : Conditions
        The reaction conditions.

    Attributes
    ----------
    conditions
    acid
    base

    Notes
    -----
    This class makes some pretty heavy assumptions about the type and format
    of the data being passed to it.  Should generally not be called directly,
    but instead from the middle layer between interface (command line or GUI)
    and the underlying framework.
    """

    _conditions = None
    _acid = ()
    _base = ()

    def __init__(self, acid, base, cond):
        self.conditions = cond
        self.acid = acid
        self.base = base

    @property
    def conditions(self):
        """The Conditions object for the reaction.

        Notes
        -----
        It is assumed that all necessary information for the reaction will be
        provided within this object (except the acid and base).
        """

        return self._conditions

    @conditions.setter
    def conditions(self, cond):
        if isinstance(cond, dict):
            self.conditions = Conditions(cond)
        elif isinstance(cond, Conditions):
            self._conditions = cond
        else:
            raise TypeError("Conditions must be a Conditions object")

    @property
    def acid(self):
        """The acid in the reaction.

        Notes
        -----
        The acid passed to the constructor may not be the one treated as an acid
        for the reaction; acidic conditions may affect the outcome.
        """

        return self._acid

    @acid.setter
    def acid(self, acid_):
        if self.conditions.acidic:
            if self.conditions.pka < acid_.pka:
                self._acid = (self.conditions.pka_molecule,
                              self.conditions.pka_location)
            else:
                self._acid = (acid_, acid_.acidic_point)
        else:
            self._acid = (acid_, acid_.acidic_point)

    @property
    def base(self):
        """The base in the reaction.

        Notes
        -----
        The base passed to the constructor may not be the one treated as an base
        for the reaction; basic conditions may affect the outcome.
        """

        return self._base

    @base.setter
    def base(self, base_):
        if self.conditions.basic:
            if self.conditions.pka > base_.pka:
                self._base = (self.conditions.pka_molecule,
                              self.conditions.pka_location)
            else:
                self._base = (base_, base_.basic_point)
        else:
            self._base = (base_, base_.basic_point)

    def _equilibrium(self, threshold=10.):
        # TODO: Check the wording of this docstring
        """Calculates what, if any, equilibrium will be reached by the reaction.

        Parameters
        ----------
        threshold : float, optional
            The pKa threshold used to determine the equilibrium.  Defaults to 10
            pKa units.

        Returns
        -------
        tuple
            A tuple storing the ratio of reactants to products.

        Raises
        ------
        NoReactionError
            Raised if the acid and base have equal pKa (and thus no reaction
            would occur).
        """

        pka1, pka2 = self.acid[0].pka, self.base[0].pka
        diff = pka1 - pka2
        if diff == 0:
            raise NoReactionError("These two molecules have identical pka")
        # TODO: This doesn't look right to me.  I think I need to fix this.
        elif diff < 0:
            if abs(diff) > threshold:
                return 1, 0
            else:
                return pow(10, abs(diff)), 1
        else:
            if diff > threshold:
                return 0, 1
            else:
                return 1, pow(10, diff)

    @staticmethod
    def _calculate_ratio(difference, threshold):
        # TODO: Check the wording of this docstring
        """Calculates the equilibrium ratio.

        Parameters
        ----------
        difference : float
            The difference between pKas.
        threshold : float
            The necessary difference.

        Returns
        -------
        float
            The amount of product there will be, relative to a value of `1` for
            the reactants.
        """

        if difference > threshold:
            return 0.0
        else:
            return pow(10, difference)

    def _calculate_products(self):
        """Determines the expected products of the reaction.

        Returns
        -------
        tuple
            A tuple of tuples.  The form is something like

                (Major Product, Minor Product)

            which can be further broken down into

                ((Conj. Acid, Conj. Base, Salt), (Empty Product))


        Notes
        -----
        This will generally be the conjugate acid and base, as well as some salt
        (or other byproduct).  This method is still incomplete - it lacks
        support for generating the salt from ionic compounds.
        """

        conjugate_acid = None
        conjugate_base = None
        salt = None   # NYI

        acid, base = deepcopy(self.acid[0]), deepcopy(self.base[0])
        conjugate_acid = base.to_conjugate_acid()
        other = acid.other_info

        try:
            other['id'] = "Conjugate base of {}".format(acid.other_info['id'])
        except KeyError:
            other['id'] = "Unknown Base"
        conjugate_base = compounds.Compound(
            *self._remove_node(acid, self.acid[1]), other_info=other)
        return ((Product(conjugate_acid, 50),
                 Product(conjugate_base, 50),
                 Product(salt, 0)),
                (Product(None, 0),))

    def react(self):
        """Performs the actual acid-base reaction.

        Returns
        -------
        Products, EquilibriumProducts
            The products of the reaction.

        Notes
        -----
        Current implementation is incomplete and only accurately describes a
        small fraction of acid-base reactions
        """

        product_ratio, reactant_ratio = self._equilibrium()
        major, minor = self._calculate_products()
        if reactant_ratio == 0:
            return Products(major, minor)
        else:
            # This doesn't work at all how it should.  Here for completeness
            return EquilibriumProducts(major, minor)
