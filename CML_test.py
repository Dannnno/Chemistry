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
        self.test_molecules = {'m1': {'bonds': {'b1': ('a1', 'a3', '1'), 'b2': ('a2', 'a3', '1')}, 'atoms': {'a1': 'H', 'a3': 'O', 'a2': 'H'}}, 'm2': {'bonds': {'b1': ('a1', 'a2', '1')}, 'atoms': {'a1': 'Na', 'a2': 'Cl'}}}
    
    def test_parse(self):
        self.parsed_molecules = {''.join(["m", str(i+1)]):CheML.CMLParser(afile).molecule for i, afile in enumerate(self.testfiles)}    
        self.assertDictEqual(self.test_molecules, self.parsed_molecules)


        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCMLParser)
unittest.TextTestRunner(sys.stdout, verbosity=2).run(suite)