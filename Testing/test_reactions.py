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


class test_acid_base(unittest.TestCase):
    
    def setUp(self):
        ## Water
        self.compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1),
                                      "b3":("a3", "a4", 1)},
                                     {"id":"Hydronium"})
        ## Ketone
        self.compound2 = cg.Compound({"a1": "H", "a2": "O"},
                                     {"b1": ("a1", "a2", 1)},
                                     {"id":"Hydroxide"})
                                     
    def test_strongacid_strongbase(self): 
    
        self.assertEqual(cg.Compound.react(self.compound1, self.compound2),
                         [cg.Compound({"a1": "H", "a2": "O", "a3": "H"},
                                     {"b1": ("a1", "a2", 1),
                                      "b2": ("a2", "a3", 1)},
                                     {}),
                          cg.Compound({"a1": "H", "a2": "O", "a3": "H"},
                                     {"b1": ("a1", "a2", 1),
                                      "b2": ("a2", "a3", 1)},
                                     {})
                         ])
        
    

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
