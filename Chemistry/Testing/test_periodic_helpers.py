# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base import _table_builder as tb


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


if __name__ == '__main__':
    from . import helper
    helper(globals())
