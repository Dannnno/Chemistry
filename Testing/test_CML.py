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

import unittest
import os
import sys
import CheML


class TestCMLParser(unittest.TestCase):
    primary_directory = os.getcwd()
      
    def setUp(self): 
        self.maxDiff = None
        os.chdir(self.primary_directory + '/molecules/test_molecules')
        self.testfiles = ["CML_1.cml", "CML_2.cml"]
        self.test_write_files = ["CML_1w.cml", "CML_2w.cml"]
        self.test_molecules = {'Water': {'bonds': {'b1': ('a1', 'a3', '1'), 'b2': ('a2', 'a3', '1')}, 'atoms': {'a1': 'H', 'a3': 'O', 'a2': 'H'}}, 'Salt': {'bonds': {'b1': ('a1', 'a2', '1')}, 'atoms': {'a1': 'Na', 'a2': 'Cl'}}}
    
    def test_parse(self):
        self.parsed_molecules = {parsed_cml.id:parsed_cml.molecule for parsed_cml in map(CheML.CMLParser, self.testfiles)}    
        self.assertDictEqual(self.test_molecules, self.parsed_molecules)

    def test_build(self):
        for cmlfile, mol_id in zip(self.test_write_files, self.test_molecules.keys()):
            CheML.CMLBuilder(self.test_molecules[mol_id], mol_id, cmlfile)
            
        try:
            with open(self.test_write_files[0], 'r') as a, \
                 open(self.test_write_files[1], 'r') as b, \
                 open(self.testfiles[0], 'r') as c, \
                 open(self.testfiles[1], 'r') as d:
              
                self.assertEqual(*map(os.path.getsize, [self.test_write_files[0], self.testfiles[0]]))
                self.assertEqual(*map(os.path.getsize, [self.test_write_files[1], self.testfiles[1]]))
                
                for line1, line2, line3, line4 in zip(a, b, c, d):
                   self.assertEqual(line1, line3)
                   self.assertEqual(line2, line4)
                 
                return   
        
        except IOError as e:
            print "Operation failed: %s" % e.strerror
            self.assertEqual(1, 2) 
            
        except OSError as e:
            print "Path %s does not exist" % e.strerror
            self.assertEqual(1, 2) 
    
    def tearDown(self):
        os.chdir(self.primary_directory)
 
if __name__ == '__main__':           
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCMLParser)
    unittest.TextTestRunner(sys.stdout, verbosity=2).run(suite)