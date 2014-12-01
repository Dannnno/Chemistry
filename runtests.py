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
import logging
import os
import sys
import unittest

import Testing


## Preparing all of the written unittests within Testing/
loader = unittest.TestLoader()
suites_list = []

for _, module in inspect.getmembers(Testing):
    for _, aclass in inspect.getmembers(module):
        try:
            if issubclass(aclass, unittest.TestCase):
                suites_list.append(loader.loadTestsFromTestCase(aclass))
        except TypeError: continue
            
big_suite = unittest.TestSuite(suites_list)

## Imports every *.py/*.pyc file in the directory (except for this one) 
## and imports it, then extracts the doctests as necessary
logging.basicConfig(stream=sys.stdout, 
                    filename=os.getcwd()+"/testLog.log",
                    level=logging.DEBUG)
local_imports = set()

for path in os.listdir(os.getcwd()):
    if ((path.endswith('.py') or path.endswith('.pyc'))):
        cut_path, _, _ = path.partition('.')
        if cut_path != "runtests":
            if cut_path not in globals():
                try:
                    globals()[cut_path] = __import__(cut_path)
                    local_imports.add(globals()[cut_path])
                except ImportError as e:
                    logging.warn(
                        "{} was not imported for doctesting".format(cut_path))
            else:
                local_imports.add(globals()[cut_path])

map(big_suite.addTests, 
    map(doctest.DocTestSuite, local_imports))
        
## Finally runs the tests
with open("a.txt", 'w') as f: 
    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    #runner = unittest.TextTestRunner(f, verbosity=1) 
    runner.run(big_suite)
