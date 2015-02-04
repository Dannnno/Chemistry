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


"""This module provides the necessary classes and helper functions to create
and manipulate the products of chemical reactions.
"""


import types

from Chemistry.base.compounds import _CompoundWrapper


class Product(_CompoundWrapper):
    """The base Product object.  Represents a compound that results from a
    chemical reaction.

    Parameters
    ----------
    comp : Compound
        The compound that is being considered a product.
    percentage : float
        What percent of the total products is represented by this compound.
    """

    _compound = None

    def __init__(self, comp, percentage):
        super(Product, self).__init__(comp)
        self.percentage = percentage


class Products(object):
    """A Products object - represents a collection of Product objects because a
    reaction usually has more than one.

    Parameters
    ----------
    maj : tuple
        Tuple of 0 or more Product objects.  Represents the major products.
    min_ : tuple
        Tuple of 0 or more Product objects.  Represents the minor products.

    Attributes
    ---------
    major
    minor
    """

    def __init__(self, maj, min_):
        self._major, self._minor = (), ()
        self.major = maj
        self.minor = min_

    @property
    def major(self):
        """The major products of a reaction.

        Expected to be a collection of Product objects.  Raises a TypeError if
        given things that are not NoneType (those are skipped) or Product
        objects
        """

        return self._major

    @major.setter
    def major(self, products):
        if not isinstance(products, types.NoneType):
            for prod in products:
                if isinstance(prod, Product):
                    if isinstance(prod.compound, types.NoneType):
                        continue
                    self._major += (prod,)
                elif isinstance(prod, types.NoneType):
                    continue
                else:
                    raise TypeError(
                        "Should be a Product, not a {}".format(type(prod)))
        else:
            raise TypeError(
                "Should be a Product, not a {}".format(type(products)))

    @property
    def minor(self):
        """The minor products of a reaction.

        Expected to be a collection of Product objects.  Raises a TypeError if
        given things that are not NoneType (those are skipped) or Product
        objects
        """

        return self._minor

    @minor.setter
    def minor(self, products):
        if not isinstance(products, types.NoneType):
            for prod in products:
                if isinstance(prod, Product):
                    if isinstance(prod._compound, types.NoneType):
                        continue
                    self._minor += (prod,)
                elif isinstance(prod, types.NoneType):
                    continue
                else:
                    raise TypeError(
                        "Should be a Product, not a {}".format(type(prod)))
        else:
            raise TypeError(
                "Should be a Product, not a {}".format(type(products)))

    def __bool__(self):
        return bool(self.minor or self.major)

    __nonzero__ = __bool__

    def __eq__(self, other):
        # Todo: I should probably come up with a real implementation here
        return False

    def __ne__(self, other):
        return not self == other


class EquilibriumProducts(object):
    """EquilibriumProducts object - much the same as a Products object
    but for reversible reactions.

    Parameters
    ----------
    reactants : tuple
        Tuple of the reactants.
    products : Products
        Products object.

    Attributes
    ----------
    products
    reactants
    """

    _reactants = None
    _products = None

    def __init__(self, reactants, products):
        self.reactants = reactants
        self.products = products

    @property
    def products(self):
        """The products of the reaction; that is the things resulting from
        the interaction of the reactants
        """

        return self._products

    @products.setter
    def products(self, prod):
        self._products = Products(*prod)

    @property
    def reactants(self):
        """The reactants in the reaction; the things that were there initially
        and that remain there after the reaction
        """

        return self._reactants

    @reactants.setter
    def reactants(self, reactant):
        self._reactants = reactant
