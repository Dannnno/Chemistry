# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.compounds import Compound
from Chemistry.base.reactants import Base, Acid


class TestIsomorphisms(unittest.TestCase):

    @classmethod
    def setUpClass(cls): pass

    @classmethod
    def tearDownClass(cls): pass

    def setUp(self):
        self.water = Compound(
            {'a1': 'H', 'a2': 'O', 'a3': 'H'},
            {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 1, 'chirality': None})},
            {'id': "Water"}
        )

    def test_isomorphism1(self):
        water2 = Compound(
            {'a1': 'H', 'a2': 'O', 'a3': 'H'},
            {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}
        )
        self.assertEquals(self.water, water2)

    def test_isomorphism2(self):
        water3 = Compound(
            {'a1': 'H', 'a3': 'O', 'a2': 'H'},
            {'b1': ('a1', 'a3', {'order': 1, 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}
        )
        self.assertEquals(self.water, water3)

    def test_isomorphism3(self):
        water4 = Compound(
            {'a1': 'H', 'a3': 'O', 'a2': 'H'},
            {'b2': ('a1', 'a3', {'order': 1, 'chirality': None}),
             'b1': ('a2', 'a3', {'order': 1, 'chirality': None})}
        )
        self.assertEquals(self.water, water4)

    def test_isomorphism4(self):
        not_water = Compound(
            {'a1': 'H', 'a3': 'O', 'a2': 'H'},
            {'b1': ('a1', 'a3', {'order': 1, 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 2, 'chirality': None})}
        )
        self.assertNotEquals(self.water, not_water)

    def test_isomorphism_acid_compound(self):
        hydronium = Compound(
            {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
            {"b1": ("a1", "a3", {'order': 1, 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1, 'chirality': None}),
             "b3": ("a3", "a4", {'order': 1, 'chirality': None})},
            {"id": "Hydronium"}
        )
        acid = Acid(hydronium, 'a1', -1.74)
        self.assertEquals(acid, hydronium)

    def test_isomorphism_base_compound(self):
        hydroxide = Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {'order': 1, 'chirality': None})},
            {"id": "Hydroxide"}
        )
        base = Base(hydroxide, 'a2', 16)
        self.assertEquals(base, hydroxide)
