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

import os
import unittest

from Chemistry.base import compounds
import Chemistry.base.periodic_table as pt
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

    def test_json_serializer_repr(self):
        self.assertEqual(compounds.Compound.json_serialize(self.compound1),
                         {'other_info': {'id': 'Water'},
                          'atoms': {'a1': 'H',
                                    'a3': 'O',
                                    'a2': 'H'},
                          'bonds': {'b1': ('a1', 'a3',
                                          {'chirality': None, 'order': 1}),
                                    'b2': ('a2', 'a3',
                                          {'chirality': None, 'order': 1})}})

    def test_json_serializer_str(self):
        self.assertEqual(
            compounds.Compound.json_serialize(self.compound1, as_str=True),
            {'other_info': {'id': 'Water'},
             'atoms': {'a1': 'H',
                       'a3': 'O',
                       'a2': 'H'},
             'bonds': {'b1': ('a1', 'a3', {'chirality': None, 'order': 1}),
                       'b2': ('a2', 'a3', {'chirality': None, 'order': 1})}})

    def test_add_node_raises_KE(self):
        with self.assertRaises(KeyError):
            self.compound1._add_node('a2', pt.get_element('H'))

    def test_add_node_(self):
        self.compound1._add_node('a4', pt.get_element('H'))
        self.assertIn('a4', self.compound1.nodes())

    def test_add_edge_raises_KE(self):
        self.compound1._add_edge(
            'b3', 'a1', 'a2', {'order':1, 'chirality':None})
        with self.assertRaises(KeyError):
            self.compound1._add_edge(
                'b3', 'a1', 'a2', {'order': 1, 'chirality': None})

    def test_add_edge_(self):
        self.compound1._add_node('a4', pt.get_element('H'))
        self.compound1._add_edge(
            'b3', 'a1', 'a4', {'order':1, 'chirality':None})
        self.assertEqual(self.compound1['a1']['a4']['key'], "b3")


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


if __name__ == '__main__':
    from . import helper
    helper(globals())
