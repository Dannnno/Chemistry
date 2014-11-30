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
    import graphs3 as Chemistry
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


class test_Compound(unittest.TestCase):
    
    def setUp(self): 
        ## Water
        self.compound1 = Chemistry.Compound(
                                {"a1":"H", "a2":"H", "a3":"O"},
                                {"b1":("a1", "a3", {'order': 1,  
                                                    'chirality': None}), 
                                 "b2":("a2", "a3", {'order': 1, 
                                                    'chirality': None})},
                                {"id":"Water"})
        ## Ketone
        self.compound2 = Chemistry.Compound(
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

    def tearDown(self): pass
    
    @classmethod
    def setUpClass(cls): pass
    
    @classmethod
    def tearDownClass(cls): pass
    
    def test_contains_element_positive(self): 
        self.assertIn('H', self.compound1)
        
    def test_contains_element_negative(self):
        self.assertNotIn('Hg', self.compound2)
        
    def test_contains_id_positive(self): 
        self.assertIn('a9', self.compound2)
        
    def test_contains_id_negative(self):
        self.assertNotIn('a9', self.compound1)
    
    def test__add_node_raises_KE(self): 
        self.assertRaises(KeyError,
                          self.compound1._add_node_,
                          *('a2', Chemistry.get_Element('H')))
                          
    def test__add_node_(self): 
        self.compound1._add_node_('a4', Chemistry.get_Element('H'))
        self.assertIn('a4', self.compound1.nodes())
    
    def test__add_edge_raises_KE(self):
        self.compound1._add_edge_('b3', 'a1', 'a2', 
                                  {'order':1, 'chirality':None})
        self.assertRaises(KeyError,
                          self.compound1._add_edge_,
                          *('b3', 'a1', 'a2', {'order':1, 'chirality':None}))
    
    def test__add_edge_(self):
        self.compound1._add_node_('a4', Chemistry.get_Element('H'))
        self.compound1._add_edge_('b1', 'a1', 'a4', 
                                  {'order':1, 'chirality':None})
        self.assertEqual(self.compound1['a1']['a4']['key'], "b1")
        
    @unittest.expectedFailure
    def test_from_CML(self):
        self.assertEqual(
                self.compound1, 
                Chemistry.Compound.from_CML(os.getcwd() + 
                                     "/molecules/test_molecules/CML_1.cml"))
                          
    
class test_linear_path_finding(unittest.TestCase):
    
    def setUp(self):
        ## Water
        self.compound1 = Chemistry.Compound(
                                {"a1":"H", "a2":"H", "a3":"O"},
                                {"b1":("a1", "a3", {'order': 1,  
                                                    'chirality': None}), 
                                 "b2":("a2", "a3", {'order': 1, 
                                                    'chirality': None})},
                                {"id":"Water"})
        ## Ketone
        self.compound2 = Chemistry.Compound(
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
              
    def test_linear_path(self): 
        self.assertEquals(self.compound1.path(('H', 'O')), 
                          set([('a1', 'a3'), ('a2', 'a3')]))
        
    def test_path_raises_TE(self):
        with self.assertRaises(TypeError):
            self.compound1.path(('H', 'O', 'H'),
                                bonds=['1'])
                          
    def test_linear_path_varargs(self):
        self.assertEquals(self.compound1.path(('H', 'O', 'H')),
                          set([('a1', 'a3', 'a2'), ('a2', 'a3', 'a1')]))

    def test_linear_path_with_bond_type(self):
        self.assertEquals(self.compound1.path(('H', 'O'),
                                              bonds=[{'order':1, 
                                                      'chirality':None}]),
                          set([('a1', 'a3'), ('a2', 'a3')]))
                          
    def test_linear_path_with_partial_bonds(self):         
        self.assertEquals(self.compound2.path(('C', 'C', 'C'),
                                              bonds=[{'order':1, 
                                                      'chirality':None},
                                                     None]),
                          set([('a7', 'a8', 'a9'), ('a9', 'a8', 'a7')]))             
        

if __name__ == '__main__':
    import types
    
                          
    test_classes_to_run = []
    for key, value in globals().items():
        if isinstance(value, (type, types.ClassType)):
            if issubclass(value, unittest.TestCase):
                test_classes_to_run.append(value)

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    big_suite.addTests(doctest.DocTestSuite(Chemistry))

    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)
