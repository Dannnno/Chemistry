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

import unittest

from Chemistry.compounds import Compound
from Chemistry.base.products import Product, Products, EquilibriumProducts


class test_product(unittest.TestCase):
    """Miscellaneous tests that don't necessarily get covered by the other tests I've written.

    This is for the Product** class, not the Product*s* class"""

    def test_getattr(self):
        comp = Compound({}, {}, {})
        prod = Product(comp, {})
        self.assertFalse('node' in vars(prod))
        self.assertTrue('node' in vars(comp))
        self.assertIs(prod.node, comp.node)

    def test_eq_compound(self):
        comp = Compound({}, {}, {})
        prod = Product(comp, {})
        self.assertEqual(prod, comp)


class test_productS(unittest.TestCase):
    """Miscellaneous tests that don't necessarily get covered by the other tests I've written.

    This is for the Product*s* class, not the Product** class"""

    def test_major_property_raises_typerror1(self):
        with self.assertRaises(TypeError):
            Products({1: 1}, 0)

    def test_major_property_raises_typerror2(self):
        with self.assertRaises(TypeError):
            Products(None, 0)

    def test_major_property_raises_typerror3(self):
        with self.assertRaises(TypeError):
            Products(0, 0)

    def test_major_property_skips_NoneTypes(self):
        self.assertTrue(Products({None: 1}, {}))

    def test_minor_property_raises_typerror1(self):
        with self.assertRaises(TypeError):
            Products({}, {1: 1})

    def test_minor_property_raises_typerror2(self):
        with self.assertRaises(TypeError):
            Products({}, None)

    def test_minor_property_raises_typerror3(self):
        with self.assertRaises(TypeError):
            Products(0, 0)

    def test_minor_property_skips_NoneTypes(self):
        self.assertTrue(Products({}, {None: 1}))


if __name__ == '__main__':
    from . import helper
    helper(globals())