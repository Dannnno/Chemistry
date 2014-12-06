"""
Copyright (c) 2014 Dan Obermiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You should have received a copy of the MIT License along with this program.
If not, see <http://opensource.org/licenses/MIT>
"""

from copy import deepcopy

from Chemistry import compounds
from Chemistry.reactions.base_reactions import Reaction, Conditions
from Chemistry.base.reactants import Reactant
from Chemistry.base.products import Product, Products, EquilibriumProducts
from Chemistry.reactions.exceptions import NoReactionError


class AcidBase(Reaction):
    _conditions = None

    def __init__(self, acid, base, cond):
        self._acid, self._base = (), ()
        self.conditions = cond
        self.acid = acid
        self.base = base

    @property
    def conditions(self):
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

    def _equilibrium(self):
        pka1, pka2 = self.acid[0].pka, self.base[0].pka
        diff = pka1-pka2
        if diff == 0:
            raise NoReactionError("These two molecules have identical pka")
        elif diff < 0:
            if abs(diff) > 10:
                return (1, 0)
            else:
                return (10**abs(diff), 1)
        else:
            if diff > 10:
                return 0, 1
            else:
                return (1, 10**diff)

    def _calculate_products(self):
        conjugate_acid = None
        conjugate_base = None
        salt = None # NYI

        acid, base = deepcopy(self.acid[0]), deepcopy(self.base[0])
        symbol = acid.node[self.acid[1]]['symbol']
        new_base_key = Reactant._new_key(base)
        new_base_bond_key = Reactant._new_key(base, False)

        conjugate_acid = base.to_conjugate_acid()
        #_Compound
        #conjugate_acid._add_node_(new_base_key, compounds.get_Element(symbol))
        #conjugate_acid._add_edge_(new_base_bond_key, self.base[1], new_base_key)
        #try:
        #    conjugate_acid.other_info['id'] = \
        #            "Conjugate acid of {}".format(base.other_info['id'])
        #except KeyError:
        #    conjugate_acid.other_info['id'] = "Unknown acid"

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
        product_ratio, reactant_ratio = self._equilibrium()
        major, minor = self._calculate_products()
        if reactant_ratio == 0:
            return Products(major, minor)
        else:
            return EquilibriumProducts(major, minor)
