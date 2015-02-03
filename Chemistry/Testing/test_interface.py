# Copyright (c) 2014 Dan Obermiller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# You should have received a copy of the MIT License along with this program.
# If not, see <http://opensource.org/licenses/MIT>


import unittest

from Chemistry.interface.reaction_utility import separate_molecules, \
    add_other_to_molecule


class TestSeparate(unittest.TestCase):

    def test_single_molecule(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                 'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}
        resulting_molecules = separate_molecules(atoms, bonds)
        self.assertEqual(len(resulting_molecules), 1)
        self.assertDictEqual(resulting_molecules[0],
                             {'atoms': {'a1': 'H', 'a2': 'O', 'a3': 'H'},
                              'bonds': {'b1': ('a1', 'a2', {'order': 1,
                                                            'chirality': None}),
                                        'b2': ('a2', 'a3', {'order': 1,
                                                            'chirality': None})}
                             })

    def test_multiple_molecules(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H',
                 'a4': 'H', 'a5': 'O', 'a6': 'H'}
        bonds = {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                 'b2': ('a2', 'a3', {'order': 1, 'chirality': None}),
                 'b3': ('a4', 'a5', {'order': 1, 'chirality': None}),
                 'b4': ('a5', 'a6', {'order': 1, 'chirality': None})}
        resulting_molecules = separate_molecules(atoms, bonds)
        self.assertEqual(len(resulting_molecules), 2)
        self.assertDictEqual(resulting_molecules[0],
                             {'atoms': {'a1': 'H', 'a2': 'O', 'a3': 'H'},
                              'bonds': {'b1': ('a1', 'a2', {'order': 1,
                                                            'chirality': None}),
                                        'b2': ('a2', 'a3', {'order': 1,
                                                            'chirality': None})}
                             })
        self.assertDictEqual(resulting_molecules[1],
                             {'atoms': {'a4': 'H', 'a5': 'O', 'a6': 'H'},
                              'bonds': {'b3': ('a4', 'a5', {'order': 1,
                                                            'chirality': None}),
                                        'b4': ('a5', 'a6', {'order': 1,
                                                            'chirality': None})}
                             })


class TestAddOther(unittest.TestCase):

    def test_other_present(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                 'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}
        resulting_molecules = separate_molecules(atoms, bonds)
        resulting_molecules[0]['other_info'] = {}
        add_other_to_molecule(resulting_molecules[0], {'name': 'Water'})
        self.assertIn('name', resulting_molecules[0]['other_info'])
        self.assertEqual('Water', resulting_molecules[0]['other_info']['name'])

    def test_other_not_present(self):
        atoms = {'a1': 'H', 'a2': 'O', 'a3': 'H'}
        bonds = {'b1': ('a1', 'a2', {'order': 1, 'chirality': None}),
                 'b2': ('a2', 'a3', {'order': 1, 'chirality': None})}
        resulting_molecules = separate_molecules(atoms, bonds)
        add_other_to_molecule(resulting_molecules[0], {'name': 'Water'})
        self.assertIn('name', resulting_molecules[0]['other_info'])
        self.assertEqual('Water', resulting_molecules[0]['other_info']['name'])
