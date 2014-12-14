#Copyright (c) 2014 Dan Obermiller
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#You should have received a copy of the MIT License along with this program.
#If not, see <http://opensource.org/licenses/MIT>


from copy import deepcopy

from Chemistry import compounds
from Chemistry.reactions.base_reactions import Reaction, Conditions
from Chemistry.base.products import Product, Products, EquilibriumProducts
from Chemistry.reactions.exceptions import NoReactionError


class AcidBase(Reaction):
    """Describes an acid-base reaction.  Creating an instance of this object
    with the appropriate variables (which is handled by the application when run
    from the GUI) will do all the necessary prep work to perform the reaction.
    """
    _conditions = None

    def __init__(self, acid, base, cond):
        self._acid, self._base = (), ()
        self.conditions = cond
        self.acid = acid
        self.base = base

    @property
    def conditions(self):
        """The Conditions object for the reaction.  Should contain enough
        information for the reaction to take place.  Not including important
        information about solvents, other present molecules and the like will
        impair the results.  Can be given a dictionary instead of a Conditions
        object - it will be transformed into a Conditions object
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
        """The compound that is being treated as an acid for this reaction. Note
        that if the conditions are acidic the compound being passed in as the
        acid may not be the one used in the reaction (if the conditions are more
        acidic than the compound that purports to be an acid).
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
        """The compound that is being treated as an base for this reaction. Note
        that if the conditions are basic the compound being passed in as the
        base may not be the one used in the reaction (if the conditions are more
        basic than the compound that purports to be an base)
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

    def _equilibrium(self, threshold=10):
        """Calculates what the equilibrium between reactants and products is,
        if any.  This comparison is done by a difference in pka between the acid
        and the conjuagte acid and the base.  By default this threshold is a
        difference of 10 pKa units.
        """
        pka1, pka2 = self.acid[0].pka, self.base[0].pka
        diff = pka1-pka2
        if diff == 0:
            raise NoReactionError("These two molecules have identical pka")
        elif diff < 0:
            if abs(diff) > threshold:
                return (1, 0)
            else:
                return (10**abs(diff), 1)
        else:
            if diff > threshold:
                return 0, 1
            else:
                return (1, 10**diff)

    def _calculate_products(self):
        """Determines the expected products of the reaction.  This will
        generally be the conjugate acid and base, as well as some salt (or other
        byproduct).  This method is still incomplete - it lacks support for
        generating the salt from ionic compounds.
        """
        conjugate_acid = None
        conjugate_base = None
        salt = None # NYI

        acid, base = deepcopy(self.acid[0]), deepcopy(self.base[0])
        conjugate_acid = base.to_conjugate_acid()
        other = acid.other_info

        try:
            other['id'] = "Conjugate base of {}".format(acid.other_info['id'])
        except KeyError:
            other['id'] = "Unknown Base"
        conjugate_base = compounds.Compound(
                            *self._remove_node(acid, self.acid[1]),
                            other_info=other)
        return ((Product(conjugate_acid, 50),
                  Product(conjugate_base, 50),
                  Product(salt, 0)),
                 (Product(None, 0),))

    def react(self):
        """Performs the actual acid-base reaction.  Current implementation is
        incomplete and only accurately describes a small fraction of acid-base
        reactions
        """
        product_ratio, reactant_ratio = self._equilibrium()
        major, minor = self._calculate_products()
        if reactant_ratio == 0:
            return Products(major, minor)
        else:
            return EquilibriumProducts(major, minor)
