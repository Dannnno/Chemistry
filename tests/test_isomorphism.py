# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base import compounds
from Chemistry.reactions._reactions import Conditions
from Chemistry.base.reactants import Base, Acid, Reactant


class TestIsomorphisms(unittest.TestCase):

    @classmethod
    def setUpClass(cls): pass

    @classmethod
    def tearDownClass(cls): pass

    def setUp(self):
        self.compound1 = compounds.Compound(
                                {"a1":"H", "a2":"O"},
                                {"b1":("a1", "a2", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydroxide"})
        self.compound2 = compounds.Compound(
                                {"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                {"b1":("a1", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b2":("a2", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b3":("a3", "a4", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydronium"})
        self.compound3 = compounds.Compound(
                                {'a1':'H', 'a2':'O', 'a3':'H'},
                                {'b1':('a1', 'a2', {'order':1,
                                                    'chirality':None}),
                                 'b2':('a2', 'a3', {'order':1,
                                                    'chirality':None})},
                                {'id':"Water"})
        self.acid = Acid(self.compound2, 'a1', -1.74)
        self.base = Base(self.compound1, 'a2', 16)
        self.conj_acid = Acid(self.compound3, 'a3', 16)
        self.conditions = Conditions({})

    def tearDown(self): pass

    def test_isomorphism1(self):
        self.compound4 = compounds.Compound(
                                {'a1':'H', 'a2':'O', 'a3':'H'},
                                {'b1':('a1', 'a2', {'order':1,
                                                    'chirality':None}),
                                 'b2':('a2', 'a3', {'order':1,
                                                    'chirality':None})})
        self.assertEquals(self.compound3, self.compound4)

    def test_isomorphism2(self):
        self.compound4 = compounds.Compound(
                                {'a1':'H', 'a3':'O', 'a2':'H'},
                                {'b1':('a1', 'a3', {'order':1,
                                                    'chirality':None}),
                                 'b2':('a2', 'a3', {'order':1,
                                                    'chirality':None})})
        self.assertEquals(self.compound3, self.compound4)

    def test_isomorphism3(self):
        self.compound4 = compounds.Compound(
                                {'a1':'H', 'a3':'O', 'a2':'H'},
                                {'b2':('a1', 'a3', {'order':1,
                                                    'chirality':None}),
                                 'b1':('a2', 'a3', {'order':1,
                                                    'chirality':None})})
        self.assertEquals(self.compound3, self.compound4)

    def test_isomorphism4(self):
        self.compound4 = compounds.Compound(
                                {'a1':'H', 'a3':'O', 'a2':'H'},
                                {'b1':('a1', 'a3', {'order':1,
                                                    'chirality':None}),
                                 'b2':('a2', 'a3', {'order':2,
                                                    'chirality':None})})
        self.assertNotEquals(self.compound3, self.compound4)

    def test_isomorphism_acid_compound(self):
        self.assertEquals(self.acid, self.compound2)

    def test_isomorphism_base_compound(self):
        self.assertEquals(self.base, self.compound1)


if __name__ == '__main__':
    from . import helper
    helper(globals())
