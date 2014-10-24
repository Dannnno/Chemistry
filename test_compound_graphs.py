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

class test_compound(unittest.TestCase): 
    
    def test_from_CML(self):
        self.assertRaises(NotImplementedError,
                          cg.Compound.from_CML,
                          "any_file_name.cml")
                          
    def test_json_serializer(self):
        self.assertEqual(cg.Compound.json_serialize(cg.Element()),
                         {'oxid': [1, 2, 3, 4, -4, -3, -2, -1], 
                          'group': 14, 'name': 'Carbon', 'weight': 12.011, 
                          'bonds': set([]), 'symbol': 'C', 'density': 2.267,
                          'number': 6, 'eneg': 2.55, 'bp': 4300.0, 
                          'bonded_to': set([]), 'radius': 67.0, 'mp': 3800.0})
        a = cg.Element()
        b = cg.Element()
        ab = cg.Bond(a, b)                          
        self.assertEqual(cg.Compound.json_serialize(ab),
                         {'second': b,
                          'first': a,
                          'chirality': None, 'order': 1, 
                          'bond': set([a,b])})
        self.assertEqual(cg.Compound.json_serialize(set([1, 2, 3])),
                         ['1', '2', '3'])


class test_element(unittest.TestCase): 
    
    def test_create_bond(self):
        a = cg.Element()
        b = cg.Element()
        ab = cg.Bond(a, b)
        a.create_bond(ab, b) # This is a bad test
                             # It really happens in Bond.__init__()
        self.assertIn(ab, a.bonds)
        self.assertIn(a, b.bonded_to)
    
    def test_break_bond(self): 
        a = cg.Element()
        b = cg.Element()
        ab = cg.Bond(a, b)
        a.break_bond(ab)
        self.assertNotIn(ab, a.bonds)
        self.assertNotIn(ab, b.bonds)
        self.assertNotIn(a, b.bonded_to)
        self.assertNotIn(b, a.bonded_to)


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

    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    runner.run(big_suite)