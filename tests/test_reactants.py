# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.compounds import Compound
from Chemistry.base.reactants import Reactant, Acid, Base


class TestReactantUtilityMethods(unittest.TestCase):

    def test_new_key1(self):
        comp = Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {'order': 1,
                                 'chirality': None})},
            {"id": "Hydroxide"}
        )
        self.assertEqual('a3', Reactant._new_key(comp))

    def test_new_key2(self):
        acid = Acid(Compound(
            {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
            {"b1": ("a1", "a3", {'order': 1,
                                 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1,
                                 'chirality': None}),
             "b3": ("a3", "a4", {'order': 1,
                                 'chirality': None})},
            {"id": "Hydronium"}), 'a1', -1.74
        )
        self.assertEqual('a5', Reactant._new_key(acid))

    def test_new_key3(self):
        base = Base(Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {'order': 1,
                                 'chirality': None})},
            {"id": "Hydroxide"}), 'a2', 16
        )
        self.assertEqual('b2', Reactant._new_key(base, False))


class TestBase(unittest.TestCase):

    def test_to_conjugate_Acid(self):
        conjugate_acid = Acid(Compound(
            {'a1': 'H', 'a2': 'O', 'a3': 'H'},
            {'b1': ('a1', 'a2', {'order': 1,
                                 'chirality': None}),
             'b2': ('a2', 'a3', {'order': 1,
                                 'chirality': None})},
            {'id': "Water"}), 'a3', 16
        )
        base = Base(Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {'order': 1,
                                 'chirality': None})},
            {"id": "Hydroxide"}), 'a2', 16
        )
        self.assertEqual(base.to_conjugate_acid(), conjugate_acid)
