# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.interface.reaction_utility import separate_molecules, \
    add_other_to_molecule


class TestSeparate(unittest.TestCase):

    def test_single_molecule(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {
            'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
            'b2': ('a2', 'a3', {'order': 1, 'chirality': None})
        }
        resulting_molecules = separate_molecules(atoms, bonds)
        self.assertEqual(len(resulting_molecules), 1)
        self.assertDictEqual(
            resulting_molecules[0],
            {
                'atoms': {'a1': 'H', 'a2': 'O', 'a3': 'H'},
                'bonds': {
                    'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                    'b2': ('a2', 'a3', {'order': 1, 'chirality': None})
                }
            }
        )

    def test_multiple_molecules(self):
        atoms = {
            'a1': 'H', 'a2': 'O', 'a3': 'H',
            'a4': 'H', 'a5': 'O', 'a6': 'H'
        }
        bonds = {
            'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
            'b2': ('a2', 'a3', {'order': 1, 'chirality': None}),
            'b3': ('a4', 'a5', {'order': 1, 'chirality': None}),
            'b4': ('a5', 'a6', {'order': 1, 'chirality': None})
        }
        resulting_molecules = separate_molecules(atoms, bonds)
        self.assertEqual(len(resulting_molecules), 2)
        self.assertDictEqual(
            resulting_molecules[0],
            {
                'atoms': {'a1': 'H', 'a2': 'O', 'a3': 'H'},
                'bonds': {
                    'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                    'b2': ('a2', 'a3', {'order': 1, 'chirality': None})
                }
            }
        )
        self.assertDictEqual(
            resulting_molecules[1],
            {
                'atoms': {'a4': 'H', 'a5': 'O', 'a6': 'H'},
                'bonds': {
                    'b3': ('a4', 'a5', {'order': 1, 'chirality': None}),
                    'b4': ('a5', 'a6', {'order': 1, 'chirality': None})
                }
            }
        )


class TestAddOther(unittest.TestCase):

    def test_other_present(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {
            'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
            'b2': ('a2', 'a3', {'order': 1, 'chirality': None})
        }
        resulting_molecules = separate_molecules(atoms, bonds)
        resulting_molecules[0]['other_info'] = {}
        add_other_to_molecule(resulting_molecules[0], {'name': 'Water'})
        self.assertIn('name', resulting_molecules[0]['other_info'])
        self.assertEqual('Water', resulting_molecules[0]['other_info']['name'])

    def test_other_not_present(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {
            'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
            'b2': ('a2', 'a3', {'order': 1, 'chirality': None})
        }
        resulting_molecules = separate_molecules(atoms, bonds)
        add_other_to_molecule(resulting_molecules[0], {'name': 'Water'})
        self.assertIn('name', resulting_molecules[0]['other_info'])
        self.assertEqual('Water', resulting_molecules[0]['other_info']['name'])
