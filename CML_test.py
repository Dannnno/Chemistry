import unittest
import os
import CheML.CheML as CheML

primary_directory = "C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry/"
os.chdir(primary_directory)

class TestCMLParser(unittest.TestCase):
    
    def setUp(self): 
        print "Setting up..."
        os.chdir("C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry/CheML/molecules/test_molecules")
        self.testfiles = ["CML_1.cml", "CML_2.cml"]
        self.test_molecules = {'m1': {'bonds': {'b1': ('a1', 'a3', '1'), 'b2': ('a2', 'a3', '1')}, 'atoms': {'a1': 'H', 'a3': 'O', 'a2': 'H'}}, 'm2': {'bonds': {'b1': ('a1', 'a2', '1')}, 'atoms': {'a1': 'Na', 'a2': 'Cl'}}}
    
    def tearDown(self): 
        print "Tearing down..."
    
    def test_parse(self):
        print "Testing CML parsing"
        self.parsed_molecules = {''.join(["m", str(i+1)]):CheML.CMLParser(afile).molecule for i, afile in enumerate(self.testfiles)}    
        self.assertDictEqual(self.test_molecules, self.parsed_molecules)
        
    def test_two(self):
        print "testing unittest"
        self.assertEqual(1, 1)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCMLParser)
unittest.TextTestRunner(verbosity=0).run(suite)