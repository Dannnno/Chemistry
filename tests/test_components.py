# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.components import Atom, Bond
from Chemistry.base.compounds import Compound
from Chemistry.base.periodic_table import periodic_table
from Chemistry.exceptions.AtomicErrors import ValenceError


class TestAtom(unittest.TestCase):

    def setUp(self):
        self.hydrogen = Atom('H')

    def test_fill_orbitals_hydrogen(self):
        self.hydrogen.fill_orbitals()
        self.assertEqual(self.hydrogen.lpe, 0)

    @unittest.expectedFailure
    def test_fill_orbitals_oxygen(self):
        oxygen = Atom('O')
        oxygen.fill_orbitals()
        self.assertEqual(oxygen.lpe, 4)

    def test_add_bond(self):
        oxygen = Atom('O')
        bond = Bond(oxygen, self.hydrogen, order=1)
        self.assertIs(bond, oxygen.bonds[0])
        self.assertIs(bond, self.hydrogen.bonds[0])

    def test_hydrogen_ion_steric_num(self):
        self.assertEqual(self.hydrogen.steric_num, 0)

    @unittest.expectedFailure
    def test_hydrogen_metal_steric_num(self):
        self.hydrogen.add_lone_pair()
        self.assertEqual(self.hydrogen.steric_num, 1)

    def test_bonded_hydrogen_steric_num(self):
        oxygen = Atom('O')
        Bond(oxygen, self.hydrogen, order=1)
        self.assertEqual(self.hydrogen.steric_num, 1)

    def test_remove_bond(self):
        oxygen = Atom('O')
        bond = Bond(oxygen, self.hydrogen, order=1)
        self.hydrogen.remove_bond(bond, other=oxygen)
        self.assertNotIn(bond, self.hydrogen.bonds)
        self.assertNotIn(bond, oxygen.bonds)

    def test_add_lone_pair(self):
        self.hydrogen.add_lone_pair()

    @unittest.expectedFailure
    def test_add_lone_pair_raises_VE(self):
        with self.assertRaises(ValenceError):
            self.hydrogen.add_lone_pair(2)

    @unittest.expectedFailure
    def test_add_lone_pair_raises_VE_if_bonded(self):
        oxygen = Atom('O')
        Bond(oxygen, self.hydrogen, order=1)
        with self.assertRaises(ValenceError):
            self.hydrogen.add_lone_pair()

    @unittest.expectedFailure
    def test_remove_lone_pair(self):
        self.hydrogen.add_lone_pair()
        self.hydrogen.remove_lone_pair()

    @unittest.expectedFailure
    def test_remove_lone_pair_raises_VE(self):
        with self.assertRaises(ValenceError):
            self.hydrogen.remove_lone_pair()


class TestGetAttr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hydrogen = Atom('H')

    def test_eneg(self):
        self.assertEqual(
            self.hydrogen.eneg, periodic_table['H']['Electronegativity']
        )
        self.assertIs(
            self.hydrogen.eneg, periodic_table['H']['Electronegativity']
        )

    def test_group(self):
        self.assertEqual(self.hydrogen.group, periodic_table['H']['Group'])
        self.assertIs(self.hydrogen.group, periodic_table['H']['Group'])

    def test_melt(self):
        self.assertEqual(
            self.hydrogen.melt, periodic_table['H']['Melting Point']
        )
        self.assertIs(self.hydrogen.melt, periodic_table['H']['Melting Point'])

    def test_mass(self):
        self.assertEqual(self.hydrogen.mass, periodic_table['H']['Weight'])
        self.assertIs(self.hydrogen.mass, periodic_table['H']['Weight'])

    def test_density(self):
        self.assertEqual(self.hydrogen.density, periodic_table['H']['Density'])
        self.assertIs(self.hydrogen.density, periodic_table['H']['Density'])

    def test_symbol(self):
        self.assertEqual(self.hydrogen.symbol, periodic_table['H']['Symbol'])
        self.assertIs(self.hydrogen.symbol, periodic_table['H']['Symbol'])

    def test_name(self):
        self.assertEqual(self.hydrogen.name, periodic_table['H']['Element'])
        self.assertIs(self.hydrogen.name, periodic_table['H']['Element'])

    def test_number(self):
        self.assertEqual(
            self.hydrogen.number, periodic_table['H']['Atomic Number']
        )
        self.assertIs(
            self.hydrogen.number, periodic_table['H']['Atomic Number']
        )

    def test_boil(self):
        self.assertEqual(
            self.hydrogen.boil, periodic_table['H']['Boiling Point']
        )
        self.assertIs(self.hydrogen.boil, periodic_table['H']['Boiling Point'])

    def test_valence(self):
        self.assertEqual(self.hydrogen.valence, periodic_table['H']['Valence'])
        self.assertIs(self.hydrogen.valence, periodic_table['H']['Valence'])

    def test_radius(self):
        self.assertEqual(
            self.hydrogen.radius, periodic_table['H']['Atomic Radius']
        )
        self.assertIs(
            self.hydrogen.radius, periodic_table['H']['Atomic Radius']
        )

    def test_oxidation(self):
        self.assertEqual(
            self.hydrogen.oxidation, periodic_table['H']['Oxidation Number(s)']
        )
        self.assertIs(
            self.hydrogen.oxidation, periodic_table['H']['Oxidation Number(s)']
        )


class TestHybridization(unittest.TestCase):

    def setUp(self):
        self.water = Compound({'a1': 'H', 'a2': 'H', 'a3': 'O'},
            {'b1': ('a1', 'a3', {'order': 1}),
             'b2': ('a2', 'a3', {'order': 1})},
            {})

    def test_water_hydrogen(self):
        self.assertEqual(self.water.atoms['a1'].hybridization, 'unhybridized')

    @unittest.expectedFailure
    def test_water_oxygen(self):
        self.assertEqual(self.water.atoms['a3'].hybridization, 'sp3')


class TestAtomicCharge(unittest.TestCase):

    def setUp(self):
        self.hydrogen = Atom('H')

    def test_hydrogen_ion_charge(self):
        self.assertEqual(self.hydrogen.charge, 1)

    @unittest.expectedFailure
    def test_hydrogen_metal_charge(self):
        self.hydrogen.add_lone_pair()
        self.assertEqual(self.hydrogen.charge, 0)

    @unittest.expectedFailure
    def test_hydrogen_bonded_charge(self):
        oxygen = Atom('O')
        oxygen.add_lone_pair(3)
        Bond(oxygen, self.hydrogen, order=1)
        self.assertEqual(self.hydrogen.charge, 0)
        self.assertEqual(oxygen.charge, -1)


class TestResonance(unittest.TestCase):

    @unittest.expectedFailure
    def test_water(self):
        water = Compound(
            {'a1': 'H', 'a2': 'H', 'a3': 'O'},
            {'b1': ('a1', 'a3', {'order': 1}),
             'b2': ('a2', 'a3', {'order': 1})},
            {}
        )

        self.assertFalse(water.resonance_structures)
        for atom in water.atoms.itervalues():
            self.assertFalse(atom.could_resonate())
        for bond in water.bonds.itervalues():
            self.assertFalse(bond.could_resonate())
