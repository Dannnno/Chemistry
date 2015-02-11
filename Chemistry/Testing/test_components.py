# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.components import Atom, Bond
from Chemistry.base.periodic_table import periodic_table
from Chemistry.exceptions.AtomicErrors import ValenceError


class TestAtom(unittest.TestCase):

    def setUp(self):
        self.atom = Atom('H')

    @unittest.expectedFailure
    def test_getattr(self):
        self.assertEqual(self.atom.eneg, periodic_table['H']['Electronegativity'])
        self.assertIs(self.atom.eneg, periodic_table['H']['Electronegativity'])

    @unittest.expectedFailure
    def test_hydrogen_ion_charge(self):
        self.assertEqual(self.atom.charge, 1)

    @unittest.expectedFailure
    def test_hydrogen_metal_charge(self):
        self.atom.add_lone_pair()
        self.assertEqual(self.atom.charge, 0)

    @unittest.expectedFailure
    def test_hydrogen_bonded_charge(self):
        oxygen = Atom('O')
        oxygen.add_lone_pair(3)
        Bond(oxygen, self.atom, order=1)
        self.assertEqual(self.atom.charge, 0)
        self.assertEqual(oxygen.charge, -1)

    def test_add_bond(self):
        oxygen = Atom('O')
        bond = Bond(oxygen, self.atom, order=1)
        self.assertIs(bond, oxygen.bonds[0])
        self.assertIs(bond, self.atom.bonds[0])

    def test_hydrogen_ion_steric_num(self):
        self.assertEqual(self.atom.steric_num, 0)

    @unittest.expectedFailure
    def test_hydrogen_metal_steric_num(self):
        self.atom.add_lone_pair()
        self.assertEqual(self.atom.steric_num, 1)

    def test_bonded_hydrogen_steric_num(self):
        oxygen = Atom('O')
        Bond(oxygen, self.atom, order=1)
        self.assertEqual(self.atom.steric_num, 1)

    def test_remove_bond(self):
        oxygen = Atom('O')
        bond = Bond(oxygen, self.atom, order=1)
        self.atom.remove_bond(bond, other=oxygen)
        self.assertNotIn(bond, self.atom.bonds)
        self.assertNotIn(bond, oxygen.bonds)

    @unittest.expectedFailure
    def test_add_lone_pair(self):
        self.atom.add_lone_pair()

    @unittest.expectedFailure
    def test_add_lone_pair_raises_VE(self):
        with self.assertRaises(ValenceError):
            self.atom.add_lone_pair(2)

    @unittest.expectedFailure
    def test_add_lone_pair_raises_VE_if_bonded(self):
        oxygen = Atom('O')
        Bond(oxygen, self.atom, order=1)
        with self.assertRaises(ValenceError):
            self.atom.add_lone_pair()

    @unittest.expectedFailure
    def test_remove_lone_pair(self):
        self.atom.add_lone_pair()
        self.atom.remove_lone_pair()

    @unittest.expectedFailure
    def test_remove_lone_pair_raises_VE(self):
        with self.assertRaises(ValenceError):
            self.atom.remove_lone_pair()
