# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base import _table_builder as tb
from Chemistry.base.periodic_table import get_element


class test_helpers(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_convert_type1(self):
        self.assertEqual(tb.convert_type('1', int), 1)

    def test_convert_type2(self):
        self.assertEqual(tb.convert_type('1.0', float), 1.0)

    def test_convert_type3(self):
        self.assertEqual(tb.convert_type('Hello', str), 'Hello')

    def test_convert_type4(self):
        self.assertEqual(tb.convert_type('[1,2,3]', tb.str_to_list), [1, 2, 3])

    def test_convert_type_bad(self):
        self.assertIsNone(tb.convert_type('No Data', int))

    def test_str_to_list1(self):
        self.assertEqual(tb.str_to_list('[1,2,3]'), ['1', '2', '3'])

    def test_str_to_list2(self):
        self.assertEqual(tb.str_to_list('[1,2,3]', mapped=int), [1, 2, 3])

    def test_build_table(self):
        self.assertFalse(tb.build_table())

    def test_get_element(self):
        self.assertDictEqual(get_element('H'),
                             {
                                 "Electronegativity": 2.2,
                                 "Group": 1,
                                 "Melting Point": 14.01,
                                 "Weight": 1.008,
                                 "Density": 8.988e-05,
                                 "Symbol": "H",
                                 "Element": "Hydrogen",
                                 "Atomic Number": 1,
                                 "Boiling Point": 20.28,
                                 "Heat of ?": 14.304,
                                 "Atomic Radius": 53.0,
                                 "Oxidation Number(s)": [
                                     1,
                                     -1
                                 ]
                             })


if __name__ == '__main__':
    from . import helper
    helper(globals())
