# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.compounds import Compound
from Chemistry.base.products import Product, Products


class TestProduct(unittest.TestCase):
    """Miscellaneous tests that don't necessarily get covered by the other tests
     I've written.

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


class TestProducts(unittest.TestCase):
    """Miscellaneous tests that don't necessarily get covered by the other tests
     I've written.

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
        self.assertFalse(Products({None: 1}, {}))

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
        self.assertFalse(Products({}, {None: 1}))


if __name__ == '__main__':
    from . import helper
    helper(globals())