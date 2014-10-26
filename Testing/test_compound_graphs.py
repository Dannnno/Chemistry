"""
Copyright (c) 2014 Dan Obermiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You should have received a copy of the MIT License along with this program.
If not, see <http://opensource.org/licenses/MIT>
"""

try:
    import cStringIO as IO
except ImportError:
    import StringIO as IO
finally:
    from collections import OrderedDict
    from functools import partial
    import compound_graphs as cg
    import contextlib
    import doctest
    import os
    import sys
    import unittest

@contextlib.contextmanager
def capture():
    oldout, olderr = sys.stdout, sys.stderr
    
    try:
        out=[IO.StringIO(), IO.StringIO()]
        sys.stdout, sys.stderr = out
        yield out
        
    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


class test_global_functions(unittest.TestCase): 

    def test_convert_type(self):
        self.assertEqual(cg.convert_type('1', int), 1)
        self.assertEqual(cg.convert_type('1.0', float), 1.0)
        self.assertEqual(cg.convert_type('Hello', str), 'Hello')
        self.assertEqual(cg.convert_type('[1,2,3]', cg.str_to_list), [1, 2, 3])
        
    def test_str_to_list(self):
        self.assertEqual(cg.str_to_list('[1,2,3]'), ['1', '2', '3'])
        self.assertEqual(cg.str_to_list('[1,2,3]', mapped=int), [1, 2, 3])

    def test_read_periodic_table(self):
        col_types = [int, str, str, int, float, float, float,
                     float, float, float, float, cg.str_to_list]
        line = ["6","C","Carbon","14","12.011","2.267","3800",
                "4300","0.709","2.55","67","[1,2,3,4,-4,-3,-2,-1]"]
        self.assertIs(os.path.exists(os.getcwd() + "/element_list.csv"), True)
        self.assertIs(isinstance(cg.read_periodic_table("element_list.csv"), 
                                 OrderedDict), True)
        self.assertEqual(cg.read_periodic_table("element_list.csv")["C"],
                         tuple((cg.convert_type(cell, typ)
                                for cell, typ in zip(line, col_types))))


class test_compound(unittest.TestCase):

    def setUp(self):
        ## Water
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1)})
        ## Ketone
        self.compound2 = cg.Compound({"a1": "H", "a2": "H", "a3": "H", 
                                      "a4": "H","a5": "H", "a6": "H", "a7": "C",
                                      "a8": "C", "a9": "C", "a10": "O"},
                                     {"b0": ("a1", "a7", 1),
                                      "b1": ("a2", "a7", 1),
                                      "b2": ("a3", "a7", 1),
                                      "b3": ("a4", "a9", 1),
                                      "b4": ("a5", "a9", 1),
                                      "b5": ("a6", "a9", 1),
                                      "b6": ("a7", "a8", 1),
                                      "b7": ("a9", "a8", 1),
                                      "b8": ("a8", "a10", 2)})

    def test_from_CML(self):
        self.assertEqual(
                self.compound1, 
                cg.Compound.from_CML(os.getcwd() + 
                                     "/molecules/test_molecules/CML_1.cml"))
                          
    def test_json_serializer_repr(self):
        self.assertEqual(cg.Compound.json_serialize(cg.Element()),
                         {'oxid': [1, 2, 3, 4, -4, -3, -2, -1], 
                          'group': 14, 'name': 'Carbon', 'weight': 12.011, 
                          'bonds': set([]), 'symbol': 'C', 'density': 2.267,
                          'number': 6, 'eneg': 2.55, 'bp': 4300.0, 
                          'ismetal': False, 'bonded_to': set([]),
                          'root': (0, 2.55), 'radius': 67.0, 'mp': 3800.0})
        a = cg.Element()
        b = cg.Element()
        ab = cg.Bond(a, b)                          
        self.assertEqual(cg.Compound.json_serialize(ab),
                         {'second': b,
                          'first': a,
                          'chirality': None, 'order': 1, 
                          'bond': set([a,b]),
                          'type': 'Non-polar covalent'})
        self.assertEqual(cg.Compound.json_serialize(set([1, 2, 3])),
                         ['1', '2', '3'])
        
        self.assertEqual(cg.Compound.json_serialize(a, as_str=True),
                         {'name': 'Carbon', 'bonded_to': ['C']})
        
        self.assertEqual(cg.Compound.json_serialize(ab, as_str=True),
                         {'first': 'C', 'second': 'C'})
                         
    def test_get_root(self):
        self.assertIs(self.compound1.root, self.compound1['a3'])
        self.assertIs(self.compound2.root, self.compound2['a8'])
        
    def test_get_item(self):
        self.assertIs(self.compound1['a1'], self.compound1.atoms['a1'])
        self.assertIs(self.compound2['b1'], self.compound2.bonds['b1'])
        self.assertRaises(KeyError, self.compound1.__getitem__, 'z3')
        self.assertRaises(KeyError, self.compound2.__getitem__, 'b9')


class test_element(unittest.TestCase): 
    
    def setUp(self):
        self.a = cg.Element()
        self.b = cg.Element()
        self.ab = cg.Bond(self.a, self.b)     
    
    def test_create_bond(self):
        self.a.create_bond(self.ab, self.b) # This is a bad test
                             # It really happens in Bond.__init__()
        self.assertIn(self.ab, self.a.bonds)
        self.assertIn(self.a, self.b.bonded_to)
    
    def test_break_bond(self): 
        self.a.break_bond(self.ab)
        self.assertNotIn(self.ab, self.a.bonds)
        self.assertNotIn(self.ab, self.b.bonds)
        self.assertNotIn(self.a, self.b.bonded_to)
        self.assertNotIn(self.b, self.a.bonded_to)
        
    def test_get_root(self):
        self.assertEquals(self.a.root, (1, self.a.eneg))
        self.assertEquals(self.b.root, (1, self.b.eneg))


class test_bond(unittest.TestCase): 

    def setUp(self): 
        self.elements = [cg.Element(), cg.Element(), cg.Element(),
                         cg.Element(), cg.Element(), cg.Element()]
        self.b1 = cg.Bond(self.elements[0], self.elements[1])
        self.b2 = (self.elements[2], self.elements[3], 4)
        self.b3 = (self.elements[4], self.elements[5], 1, 'W')
    
    def test_constructor(self):
        ## Testing that it throws a ValueError when it should
        self.assertRaises(ValueError, cg.Bond, *self.b2)
        self.assertRaises(ValueError, cg.Bond, *self.b3)
        
        ## Testing that its updating the Elements' sets
        self.assertIn(self.b1, self.elements[0].bonds)
        self.assertIn(self.elements[1], self.elements[0].bonded_to)
        
    def test_get_other(self):
        self.assertEqual(self.b1.first, self.b1.get_other(self.b1.second))
        self.assertRaises(KeyError, self.b1.get_other, self.elements[3])
        
    def test_eval_bond(self):
        self.assertEqual(self.b1.type, "Non-polar covalent")


if __name__ == '__main__':
    test_classes_to_run = [test_global_functions, 
                           test_compound, 
                           test_element, 
                           test_bond]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    big_suite.addTests(doctest.DocTestSuite(cg))

    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)