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
    import doctest
    import sys
    import unittest
    import table_builder as tb
    
    
class test_helpers(unittest.TestCase):
    
    def setUp(self): pass
    
    def tearDown(self): pass
    
    @unittest.expectedFailure
    def test_periodic_table(self):
        ## Also tests table_builder.build_table()
        tb.build_table()
        self.assertRaises(ImportError, __import__, "periodic_table")
        
    def test_convert_type(self):
        self.assertEqual(tb.convert_type('1', int), 1)
        self.assertEqual(tb.convert_type('1.0', float), 1.0)
        self.assertEqual(tb.convert_type('Hello', str), 'Hello')
        self.assertEqual(tb.convert_type('[1,2,3]', tb.str_to_list), [1, 2, 3])
     
    def test_str_to_list(self):
        self.assertEqual(tb.str_to_list('[1,2,3]'), ['1', '2', '3'])
        self.assertEqual(tb.str_to_list('[1,2,3]', mapped=int), [1, 2, 3])


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
    big_suite.addTests(doctest.DocTestSuite(tb))

    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)