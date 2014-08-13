import unittest
import os
import sys
import CheML.CheML as CheML

primary_directory = "C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry/"
os.chdir(primary_directory)

class TestCMLParser(unittest.TestCase):
    
    def setUp(self): 
        self.maxDiff = None
        os.chdir("C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry/CheML/molecules/test_molecules")
        self.testfiles = ["CML_1.cml", "CML_2.cml"]
        self.test_write_files = ["CML_1w.cml", "CML_2w.cml"]
        self.test_molecules = {'Water': {'bonds': {'b1': ('a1', 'a3', '1'), 'b2': ('a2', 'a3', '1')}, 'atoms': {'a1': 'H', 'a3': 'O', 'a2': 'H'}}, 'Salt': {'bonds': {'b1': ('a1', 'a2', '1')}, 'atoms': {'a1': 'Na', 'a2': 'Cl'}}}
    
    def test_parse(self):
        self.parsed_molecules = {CheML.CMLParser(afile).id:CheML.CMLParser(afile).molecule for i, afile in enumerate(self.testfiles)}    
        self.assertDictEqual(self.test_molecules, self.parsed_molecules)

    def test_build(self):
        for cmlfile, molecule in zip(self.test_write_files, self.test_molecules):
            CheML.CMLBuilder({molecule:self.test_molecules[molecule]}, cmlfile)
            
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
            print "Path %s does not exist" %e.strerror
            self.assertEqual(1, 2) 
            
suite = unittest.TestLoader().loadTestsFromTestCase(TestCMLParser)
unittest.TextTestRunner(sys.stdout, verbosity=2).run(suite)