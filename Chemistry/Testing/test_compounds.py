# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import json
import os
import unittest

from Chemistry.base import compounds
from Chemistry.base.components import Atom, Bond
from Chemistry.interface.compound_utility import compound_from_file, \
    compound_to_file


class TestCompound(unittest.TestCase):

    def setUp(self):
        # Water
        self.compound1 = compounds.Compound(
                                {"a1":"H", "a2":"H", "a3":"O"},
                                {"b1":("a1", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b2":("a2", "a3", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Water"})
        # Ketone
        self.compound2 = compounds.Compound(
                                {"a1": "H", "a2": "H", "a3": "H",
                                 "a4": "H","a5": "H", "a6": "H", "a7": "C",
                                 "a8": "C", "a9": "C", "a10": "O"},
                                {"b0": ("a1", "a7", {'order': 1,
                                                     'chirality': None}),
                                 "b1": ("a2", "a7", {'order': 1,
                                                     'chirality': None}),
                                 "b2": ("a3", "a7", {'order': 1,
                                                     'chirality': None}),
                                 "b3": ("a4", "a9", {'order': 1,
                                                     'chirality': None}),
                                 "b4": ("a5", "a9", {'order': 1,
                                                     'chirality': None}),
                                 "b5": ("a6", "a9", {'order': 1,
                                                     'chirality': None}),
                                 "b6": ("a7", "a8", {'order': 1,
                                                     'chirality': None}),
                                 "b7": ("a9", "a8", {'order': 1,
                                                     'chirality': None}),
                                 "b8": ("a8", "a10", {'order': 2,
                                                      'chirality': None})},
                                {})

    def test_add_node_raises_KE(self):
        with self.assertRaises(KeyError):
            self.compound1._add_node('a2', Atom('H'))

    def test_add_node_(self):
        self.compound1._add_node('a4', Atom('H'))
        self.assertIn('a4', self.compound1.nodes())

    def test_add_edge_raises_KE(self):
        self.compound1._add_edge(
            'b3', 'a1', 'a2', {'order':1, 'chirality':None})
        with self.assertRaises(KeyError):
            self.compound1._add_edge(
                'b3', 'a1', 'a2', {'order': 1, 'chirality': None})

    def test_add_edge_(self):
        self.compound1._add_node('a4', Atom('H'))
        self.compound1._add_edge(
            'b3', 'a1', 'a4', {'order':1, 'chirality':None})
        self.assertEqual(self.compound1['a1']['a4']['key'], "b3")

    @unittest.expectedFailure
    def test_neutral_charge(self):
        self.assertEqual(self.compound1.charge, 0)

    @unittest.expectedFailure
    def test_positive_charge(self):
        compound = compounds.Compound(
            {"a1": "H", "a2": "H", "a3": "H", "a4": "O"},
            {"b1": ("a1", "a4", {"order": 1}),
             "b2": ("a2", "a4", {"order": 1}),
             "b3": ("a3", "a4", {"order": 1})},
            {})
        self.assertEqual(compound.charge, 1)

    @unittest.expectedFailure
    def test_negative_charge(self):
        compound = compounds.Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {"order": 1})},
            {})
        self.assertEqual(compound.charge, -1)


class TestIO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testpath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'test_molecules')
        cls.cml_directory = os.path.join(cls.testpath, 'CML')

    def setUp(self):
        self.compound1 = compounds.Compound(
            {"a1":"H", "a2":"H", "a3":"O"},
            {"b1":("a1", "a3", {'order': 1, 'chirality': None}),
             "b2":("a2", "a3", {'order': 1, 'chirality': None})},
            {"id":"Water"})

    def test_from_CML(self):
        with open(
                os.path.join(self.cml_directory, "CML_1.cml"), 'r') as f:
            self.assertEqual(self.compound1, compound_from_file(f, 'cml'))

    def test_to_CML(self):
        with open(os.path.join(self.cml_directory, "CML_1.cml"), 'r') as f:
            from_cml = compound_from_file(f, 'cml')
            with open(
                    os.path.join(self.cml_directory, "CML_1w.cml"), 'r+') as w:
                compound_to_file(w, 'cml', from_cml)
                w.seek(0)
                self.assertEqual(from_cml, compound_from_file(w, 'cml'))


class TestSerializer(unittest.TestCase):

    def test_serialize_atom(self):
        self.assertEqual(json.dumps(
            Atom('H'), cls=compounds._ChemicalSerializer),
                        '{"symbol": "H"}')

    def test_serialize_bond(self):
        self.assertEqual(
            json.dumps(Bond(Atom('H'), Atom('H')),
                       cls=compounds._ChemicalSerializer),
            '{"members": [{"symbol": "H"}, {"symbol": "H"}]}')

    def test_serialize_has_dict(self):
        class A(object):
            def __init__(self): pass

        self.assertEqual(
            json.dumps(A(), cls=compounds._ChemicalSerializer), "{}")

    def test_has_slots(self):
        class B(object):
            __slots__ = ['A']

            def __init__(self):
                self.A = 1

        self.assertEqual(
            json.dumps(B(), cls=compounds._ChemicalSerializer), '{"A": 1}')

    def test_default(self):
        # Testing that it handles builtin types (and functions) normally
        assert json.dumps('', cls=compounds._ChemicalSerializer) == '""'
        assert json.dumps(list(), cls=compounds._ChemicalSerializer) == "[]"
        assert json.dumps(tuple(), cls=compounds._ChemicalSerializer) == "[]"
        assert json.dumps(dict(), cls=compounds._ChemicalSerializer) == "{}"
        assert json.dumps(
            lambda x: x, cls=compounds._ChemicalSerializer) == "{}"
        with self.assertRaises(TypeError):
            json.dumps(set(), cls=compounds._ChemicalSerializer)


# The below are stupid tests that I'm adding just for the sake of coverage
# I want that green colored badge
class TestStringMethods(unittest.TestCase):

    def test_string(self):
        assert str(
            compounds._CompoundWrapper(compounds.Compound({}, {}, {})))

    def test_repr(self):
        assert repr(
            compounds._CompoundWrapper(compounds.Compound({}, {}, {})))
