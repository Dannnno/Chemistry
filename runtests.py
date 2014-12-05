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

import doctest
import inspect
import os
import sys
import unittest

from Chemistry import Testing


class _DocTester(object):
    visited = {}
    
    def __init__(self):
        self.cwd = os.getcwd()
        try:
            os.chdir(os.path.join(self.cwd, 'Chemistry'))
            self.inner()
        finally:
            os.chdir(self.cwd)
    
    def inner(self, path=None):
        if path is None:
            path = os.getcwd()
        for file_ in os.listdir(path):
            if os.path.isdir(file_):
                self.inner(os.path.join(path, file_))
            else:
                f, _, suffix = file_.partition('.')
                if suffix in ['py', 'pyc'] and f not in self.visited:
                        self.visited[f] = os.path.join(path, file_)


def load_unit_tests():
    loader = unittest.TestLoader()
    suites_list = []
    for _, module in inspect.getmembers(Testing):
        for _, aclass in inspect.getmembers(module):
            try:
                if issubclass(aclass, unittest.TestCase):
                    suites_list.append(loader.loadTestsFromTestCase(aclass))
            except TypeError: continue
                
    big_suite = unittest.TestSuite(suites_list)
    return big_suite


def load_doc_tests(big_suite):
    sys.path.insert(0, '')
    tester = _DocTester()
    cwd = os.getcwd()
    try:
        for file_, path in tester.visited.iteritems(): 
            try:
                p = path[:path.rfind(os.sep)]
                sys.path[0] = p
                module = __import__(file_)
                big_suite.addTest(doctest.DocTestSuite(module))         
            except ImportError as e:
                print e
    finally:
        os.chdir(cwd)
        del sys.path[0]

    return big_suite
        

def main(use_stream=True, stream=sys.stdout, 
         file_=None, verb=1):
    test_suite = load_unit_tests()
    test_suite = load_doc_tests(test_suite)
    if use_stream:
        runner = unittest.TextTestRunner(stream, verbosity=verb)
        runner.run(test_suite)
    else:
        runner = unittest.TextTestRunner(file_, verbosity=verb)
        runner.run(test_suite)
        
        
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
                        description="Runs the unit and doc tests of Chemistry")
    parser.add_argument('-f', '--filename', dest='file_', 
                        default='test_results.log',
                        help="Filename of optional file.")
    parser.add_argument('-v', '--verbosity', dest='verb',
                        type=int, choices=[1, 2], 
                        default=1, help="Verbosity of the test output.")
    parser.add_argument('-u', '--stream', dest='use_stream',
                        action='store_false', default=True,
                        help="Whether or not to use std.out or a file")
    
    args = parser.parse_args()
    main(**vars(args))
