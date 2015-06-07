# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


from Chemistry.base.compounds import Compound
from Chemistry.base.reactants import Reactant, Acid, Base
from Chemistry.reactions._reactions import Conditions

import unittest


class TestReactantUtilityMethods(unittest.TestCase):

    def setUp(self):
        self.compound1 = Compound(
                                {"a1": "H", "a2": "O"},
                                {"b1": ("a1", "a2", {'order': 1,
                                                     'chirality': None})},
                                {"id": "Hydroxide"})
        self.compound2 = Compound(
                                {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
                                {"b1": ("a1", "a3", {'order': 1,
                                                     'chirality': None}),
                                 "b2": ("a2", "a3", {'order': 1,
                                                     'chirality': None}),
                                 "b3": ("a3", "a4", {'order': 1,
                                                     'chirality': None})},
                                {"id": "Hydronium"})
        self.acid1 = Acid(self.compound2, 'a1', -1.74)
        self.base1 = Base(self.compound1, 'a2', 16)

    def test_new_key1(self):
        self.assertEqual('a3', Reactant._new_key(self.compound1))

    def test_new_key2(self):
        self.assertEqual('a5', Reactant._new_key(self.acid1))

    def test_new_key3(self):
        self.assertEqual('b2', Reactant._new_key(self.base1, False))


class TestBase(unittest.TestCase):

    def setUp(self):
        self.compound1 = Compound(
                                {"a1": "H", "a2": "O"},
                                {"b1": ("a1", "a2", {'order': 1,
                                                     'chirality': None})},
                                {"id": "Hydroxide"})
        self.compound2 = Compound(
                                {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
                                {"b1": ("a1", "a3", {'order': 1,
                                                     'chirality': None}),
                                 "b2": ("a2", "a3", {'order': 1,
                                                     'chirality': None}),
                                 "b3": ("a3", "a4", {'order': 1,
                                                     'chirality': None})},
                                {"id": "Hydronium"})
        self.compound3 = Compound(
                                {'a1': 'H', 'a2': 'O', 'a3': 'H'},
                                {'b1': ('a1', 'a2', {'order': 1,
                                                     'chirality': None}),
                                 'b2': ('a2', 'a3', {'order': 1,
                                                     'chirality': None})},
                                {'id': "Water"})

        self.acid = Acid(self.compound2, 'a1', -1.74)
        self.base = Base(self.compound1, 'a2', 16)
        self.conj_acid = Acid(self.compound3, 'a3', 16)
        self.conditions = Conditions({})

    def test_to_conjugate_Acid(self):
        self.assertEqual(self.base.to_conjugate_acid(), self.conj_acid)
