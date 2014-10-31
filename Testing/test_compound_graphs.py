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


class test_linear_paths(unittest.TestCase):
    
    def setUp(self):
        ## Water
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1)},
                                     {"id":"Water"})
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
                                      "b8": ("a8", "a10", 2)},
                                     {})     
    
    def test_contains(self): 
        self.assertIn(cg.Element('H'), self.compound1)
        self.assertNotIn(cg.Element('Hg'), self.compound2)        
              
    def test_linear_path(self): 
        self.assertEquals(self.compound1.path(cg.Element('H'), 
                                              cg.Element('O')), 
                          [['a1', 'a3'], ['a2', 'a3']])
                          
    def test_path_raises_TE(self):
        self.assertRaises(TypeError, self.compound1.path, (1,))
        
    def test_path_raises_VE(self):
        with self.assertRaises(ValueError):
            self.compound1.path(cg.Element('H'),
                                cg.Element('O'),
                                cg.Element('H'),
                                bonds=['1'])
                          
    def test_linear_path_varargs(self):
        self.assertEquals(self.compound1.path(cg.Element('H'),
                                              cg.Element('O'),
                                              cg.Element('H')),
                          [['a1', 'a3', 'a2'], ['a2', 'a3', 'a1']])
    
    def test_linear_path_with_bond_type(self):
        self.assertEquals(self.compound1.path(cg.Element('H'),
                                              cg.Element('O'),
                                              bonds=[{'order':1, 
                                                      'chirality':None}]),
                          [['a1', 'a3'], ['a2', 'a3']])      
                          
    def test_linear_path_with_partial_bonds(self):
         self.assertEquals(self.compound2.path(cg.Element('C'),
                                               cg.Element('C'),
                                               cg.Element('C'),
                                               bonds=[{'order':1, 
                                                       'chirality':None},
                                                      None]),
                           [['a1', 'a3'], ['a2', 'a3']]) 
                                              
    def test_linear__path_helper_with_bonds(self):
        ## These helper methods will be generators, so the list is necessary
        self.assertEquals(list(self.compound1._path_helper_with_bonds(
                                    [cg.Element('H'), cg.Element('O')], 
                                    [{'order':1, 'chirality':None}]
                                                                )),
                          [['a1', 'a3'], ['a2', 'a3']]) 
        
    def test_linear__path_helper(self):
        self.assertEquals(list(self.compound1._path_helper(
                            [cg.Element('H'), cg.Element('O'), cg.Element('H')]
                                                     )),
                          [['a1', 'a3', 'a2'], ['a2', 'a3', 'a1']])  


class test_branched_paths(unittest.TestCase):

    def setUp(self):
        ## Water
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1)},
                                     {"id":"Water"})
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
                                      "b8": ("a8", "a10", 2)},
                                     {})
                                     
    def test_branching_path(self): 
        self.assertEquals(self.compound1.path(cg.Element('O'),
                                              [cg.Element('H'),
                                               cg.Element('H')]),
                          [['a3', ['a1', 'a2']], ['a3', ['a1', 'a2']]])
                          
    def test_nested_branching_path(self): 
        self.assertEquals(self.compound2.path(cg.Element('C'),
                                              [cg.Element('O'),
                                               [cg.Element('C'),
                                                [cg.Element('H')]],
                                               cg.Element('C')]),
                          [['a8', ['a10', ['a7', 'a1'], 'a9']],
                           ['a8', ['a10', ['a7', 'a2'], 'a9']],
                           ['a8', ['a10', ['a7', 'a3'], 'a9']],
                           ['a8', ['a10', ['a9', 'a4'], 'a7']],
                           ['a8', ['a10', ['a9', 'a5'], 'a7']],
                           ['a8', ['a10', ['a9', 'a6'], 'a7']]])
    
    def test_branching_path_with_bond_type(self): 
        self.assertEquals(self.compound1.path(cg.Element('O'),
                                              [cg.Element('H'),
                                               cg.Element('H')],
                                              bonds=[{'order':1, 
                                                      'chirality':None},
                                                     {'order':1, 
                                                      'chirality':None}]),
                          [['a3', ['a1', 'a2']], ['a3', ['a1', 'a2']]]) 
                          
    def test_branching_path_with_partial_bonds(self):
        self.assertEquals(self.compound1.path(cg.Element('O'),
                                              [cg.Element('H'),
                                               cg.Element('H')],
                                              bonds=[None,
                                                     {'order':1, 
                                                      'chirality':None}]),
                          [['a3', ['a1', 'a2']], ['a3', ['a1', 'a2']]])
                             
    def test_branching__path_helper_with_bonds(self): 
        self.assertEquals(list(self.compound1._path_helper_with_bonds(
                                cg.Element('O'),
                                [cg.Element('H'),
                                 cg.Element('H')],
                                bonds=[{'order':1, 
                                        'chirality':None},
                                       {'order':1, 
                                        'chirality':None}])),
                          [['a3', ['a1', 'a2']], ['a3', ['a1', 'a2']]])            
        
    def test_branching__path_helper(self): 
        self.assertEquals(list(self.compound1._path_helper(
                                    cg.Element('O'),
                                    [cg.Element('H'),
                                     cg.Element('H')])),
                          [['a3', ['a1', 'a2']], ['a3', ['a1', 'a2']]])                                     
                          

class test_ring_compounds(unittest.TestCase):
    
    def setUp(self):
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1)},
                                     {"id":"Water"})
        self.compound2 = cg.Compound({"a1":"C", "a2":"C", "a3":"C"},
                                     {"b1":("a1", "a2", 1), 
                                      "b2":("a2", "a3", 1),
                                      "b3":("a3", "a1", 1)},
                                     {})
        self.compound3 = cg.Compound({"a1":"C", "a2":"C", "a3":"C",
                                      "a4":"C", "a5":"C", "a6":"C",
                                      "a7":"H", "a8":"H", "a9":"H", 
                                      "a10":"H", "a11":"H", "a12":"H", 
                                      "a13":"H", "a14":"H", "a15":"H", 
                                      "a16":"H", "a17":"H", "a18":"H"},
                                     {"b1":("a1", "a2", 1),
                                      "b2":("a2", "a3", 1),
                                      "b3":("a3", "a4", 1),
                                      "b4":("a4", "a5", 1),
                                      "b5":("a5", "a6", 1),
                                      "b6":("a6", "a1", 1),
                                      "b7":("a6", "a7", 1),
                                      "b8":("a6", "a8", 1),
                                      "b9":("a5", "a9", 1),
                                      "b10":("a5", "a10", 1),
                                      "b11":("a4", "a11", 1),
                                      "b12":("a4", "a12", 1),
                                      "b13":("a3", "a13", 1),
                                      "b14":("a3", "a14", 1),
                                      "b15":("a2", "a15", 1),
                                      "b16":("a2", "a16", 1),
                                      "b17":("a1", "a17", 1),
                                      "b18":("a1", "a18", 1)},
                                    {})
        self.compound4 = cg.Compound({"a1":"C", "a2":"C", "a3":"C",
                                      "a4":"C", "a5":"C", "a6":"C",
                                      "a7":"H", "a8":"H", "a9":"H", 
                                      "a10":"H", "a11":"H", "a12":"H", 
                                      "a13":"H", "a14":"H", "a15":"H", 
                                      "a16":"H", "a17":"H", "a18":"Cl"},
                                     {"b1":("a1", "a2", 1),
                                      "b2":("a2", "a3", 1),
                                      "b3":("a3", "a4", 1),
                                      "b4":("a4", "a5", 1),
                                      "b5":("a5", "a6", 1),
                                      "b6":("a6", "a1", 1),
                                      "b7":("a6", "a7", 1),
                                      "b8":("a6", "a8", 1),
                                      "b9":("a5", "a9", 1),
                                      "b10":("a5", "a10", 1),
                                      "b11":("a4", "a11", 1),
                                      "b12":("a4", "a12", 1),
                                      "b13":("a3", "a13", 1),
                                      "b14":("a3", "a14", 1),
                                      "b15":("a2", "a15", 1),
                                      "b16":("a2", "a16", 1),
                                      "b17":("a1", "a17", 1),
                                      "b18":("a1", "a18", 1)},
                                    {})                                 
        
    def test_has_cycles(self):
        self.assertIs(self.compound1.has_cycles, False)
        self.assertIs(self.ccompound2.has_cycles, True)
        
    def test_get_cycles(self): 
        self.assertIs(self.compound1.get_cycles(), [set()])
        self.assertEqual(self.compound2.get_cycles(), [set(['a1', 'a2', 'a3'])])   
    
    def test_ring_path(self): 
        self.assertEqual(self.compound3.path(cg.Element(), cg.Element(), 
                                             cg.Element(), cg.Element(), 
                                             cg.Element(), cg.Element(),
                                             ring=True),
                         ## A cyclical structure should be in a tuple
                         ## not a list, and it should start/end on the 
                         ## same item
                         [('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a1')])
    
    def test_branching_ring_path(self): 
        self.assertEqual(self.compound4.path(cg.Element(), cg.Element(), 
                                             cg.Element(), 
                                             [cg.Element(), cg.Element('Cl')], 
                                             cg.Element(), cg.Element()),
                         [(['a1', 'a18'], 'a2', 'a3', 'a4', 'a5', 'a6', ['a1', 'a18'])])
    
    def test_ring_path_with_bond_type(self): 
        self.assertEqual(self.compound3.path(cg.Element(), cg.Element(), 
                                             cg.Element(), cg.Element(), 
                                             cg.Element(), cg.Element(),
                                             bonds=[None, None, None,
                                                    {'order':1, 
                                                     'chirality':None},
                                                    None, None]),
                         [('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a1')])           
                             
    def test_ring__path_helper_with_bonds(self): 
        raise NotImplementedError("I don't think these will be the helper functions, but honestly I'm not at a point where I can decide that yet")
        
    def test_ring__path_helper(self): 
        raise NotImplementedError("I don't think these will be the helper functions, but honestly I'm not at a point where I can decide that yet")
            
        
class test_compound(unittest.TestCase):

    def setUp(self):
        ## Water
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1)},
                                     {"id":"Water"})
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
                                      "b8": ("a8", "a10", 2)},
                                     {})
                                      
        self.a = cg.Element()
        self.b = cg.Element()
        self.ab = cg.Bond(self.a, self.b) 

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
                                              
        self.assertEqual(cg.Compound.json_serialize(self.ab),
                         {'second': self.b,
                          'first': self.a,
                          'chirality': None, 'order': 1, 
                          'bond': set([self.a, self.b]),
                          'type': 'Non-polar covalent'})
                         
    def test_json_serializer_str(self):
        self.assertEqual(cg.Compound.json_serialize(set([1, 2, 3])),
                         ['1', '2', '3'])
        
        self.assertEqual(cg.Compound.json_serialize(self.a, as_str=True),
                         {'name': 'Carbon', 'bonded_to': ['C']})
        
        self.assertEqual(cg.Compound.json_serialize(self.ab, as_str=True),
                         {'first': 'C', 'second': 'C'})                         
                         
    def test_get_root(self):
        self.assertIs(self.compound1.root, self.compound1['a3'])
        self.assertIs(self.compound2.root, self.compound2['a8'])
        
    def test_getitem_goodvalues(self):
        self.assertIs(self.compound1['a1'], self.compound1.atoms['a1'])
        self.assertIs(self.compound2['b1'], self.compound2.bonds['b1'])
        
    def test_getitem_badvalues(self):
        self.assertRaises(KeyError, self.compound1.__getitem__, 'z3')
        self.assertRaises(KeyError, self.compound2.__getitem__, 'b9')
        
    def test_constructor_sorting(self):
        a, b, c = cg.Element('H'), cg.Element('H'), cg.Element('O')
        ac, bc = cg.Bond(a, c), cg.Bond(b, c)
        
        self.assertEqual(self.compound1.atoms, 
                         OrderedDict((("a1", a),
                                      ("a2", b),
                                      ("a3", c))))
                                      
        self.assertEqual(self.compound1.bonds,
                         OrderedDict((("b1", ac),
                                      ("b2", bc))))
                                      
    def test_to_cml(self):
        from_cml = cg.Compound.from_CML(os.getcwd() + 
                                        "/molecules/test_molecules/CML_1.cml")
        from_cml.to_cml(os.getcwd() + "/molecules/test_molecules/CML_1w.cml")
        self.assertEqual(from_cml, 
                         cg.Compound.from_CML(os.getcwd() + 
                                    "/molecules/test_molecules/CML_1w.cml"))
        
    def test_get_key(self):
        self.assertEqual('a1', 
                         self.compound1.get_key(
                                self.compound1.atoms['a1']
                                               ))                              
        

class test_element(unittest.TestCase): 
    
    def setUp(self):
        self.a = cg.Element()
        self.b = cg.Element()
        self.c = cg.Element('O')
        self.ab = cg.Bond(self.a, self.b)     
    
    def test_create_bond(self):
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
        
    def test_rich_comparisons(self):
        self.assertLess(self.a, self.c)
        
        self.assertLessEqual(self.a, self.b)
        self.assertLessEqual(self.a, self.c)
        
        self.assertGreater(self.c, self.a)
        
        self.assertGreaterEqual(self.c, cg.Element('O'))
        self.assertGreaterEqual(self.c, self.a)
        

class test_bond(unittest.TestCase): 

    def setUp(self): 
        self.elements = [cg.Element(), cg.Element(), cg.Element(),
                         cg.Element(), cg.Element(), cg.Element()]
        self.b1 = cg.Bond(self.elements[0], self.elements[1])
        self.b2 = (self.elements[2], self.elements[3], 4)
        self.b3 = (self.elements[4], self.elements[5], 1, 'W')
    
    def test_constructor_ValueError(self):
        """Testing that it throws a ValueError when it should"""
        self.assertRaises(ValueError, cg.Bond, *self.b2)
        self.assertRaises(ValueError, cg.Bond, *self.b3)
        
    def test_constructor_updates_elements(self):
        """Testing that its updating the Elements' sets"""
        self.assertIn(self.b1, self.elements[0].bonds)
        self.assertIn(self.elements[1], self.elements[0].bonded_to)
        
    def test_get_other_good_value(self):
        self.assertEqual(self.b1.first, self.b1.get_other(self.b1.second))
        
    def test_get_other_KeyError(self):
        self.assertRaises(KeyError, self.b1.get_other, self.elements[3])
        
    def test_eval_bond(self):
        self.assertEqual(self.b1.type, "Non-polar covalent")
        
    def test_getitem(self):
        self.assertEqual(self.b1[0], self.b1.first)
        self.assertEqual(self.b1[1], self.b1.second)
        
    def test_membership(self):
        """Testing equals-a not is-a"""
        self.assertIn(self.elements[0], self.b1)
        self.assertNotIn(cg.Element('He'), self.b1)
        
    @unittest.expectedFailure
    def test_alternate_membership(self):
        """Testing is-a not equals-a"""
        self.assertIn(self.elements[0], self.b1)
        self.assertNotIn(self.elements[3], self.b1)
        
    def test_rich_comparisons(self):
        self.assertLess(self.b1, cg.Bond(cg.Element(), cg.Element(), 2))
        
        self.assertLessEqual(self.b1, cg.Bond(cg.Element(), cg.Element(), 2))
        self.assertLessEqual(cg.Bond(cg.Element(), cg.Element(), 2), 
                             cg.Bond(cg.Element(), cg.Element(), 2))
                             
        self.assertGreater(cg.Bond(cg.Element(), cg.Element(), 2), self.b1)
        
        self.assertGreaterEqual(cg.Bond(cg.Element(), cg.Element(), 2), self.b1)
        self.assertGreaterEqual(cg.Bond(cg.Element(), cg.Element(), 2), 
                                cg.Bond(cg.Element(), cg.Element(), 2))


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
    big_suite.addTests(doctest.DocTestSuite(cg))

    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)
