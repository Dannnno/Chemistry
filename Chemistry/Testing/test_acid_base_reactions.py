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
    import sys
    import unittest
    
    from Chemistry import compounds, base_reactions
    from Chemistry.base_reactions import Acid, Base, Reaction, Conditions
    from Chemistry.reactions.acid_base import AcidBase
    
        
class test_AcidBase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): pass
    
    @classmethod
    def tearDownClass(cls): pass
    
    def setUp(self): 
        self.compound1 = compounds.Compound(
                                {"a1":"H", "a2":"O"},
                                {"b1":("a1", "a2", {'order': 1,  
                                                    'chirality': None})},
                                {"id":"Hydroxide"})
        self.compound2 = compounds.Compound(
                                {"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                {"b1":("a1", "a3", {'order': 1,  
                                                    'chirality': None}), 
                                 "b2":("a2", "a3", {'order': 1, 
                                                    'chirality': None}),
                                 "b3":("a3", "a4", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydronium"})
        self.acid = Acid(self.compound2, 'a1', -1.74)
        self.base = Base(self.compound1, 'a2', 16)
        self.conditions = Conditions(**{'reactants': (self.acid, self.base)})
    
    def tearDown(self): pass
    
    def test_constructor_raises_TE1(self): 
        with self.assertRaises(TypeError):
            AcidBase(self.compound2, self.compound1, {})
    
    def test_constructor_raises_TE2(self): 
        with self.assertRaises(TypeError):
            AcidBase(self.acid, self.compound1, {})
                          
    def test_constructor_raises_TE3(self):
        with self.assertRaises(TypeError):
            AcidBase(self.acid, self.base, {})
    
    def test_good_constructor(self): 
        AcidBase(self.acid, self.base, self.conditions)
    

if __name__ == '__main__':
    import types
    
                          
    test_classes_to_run = [value for key, value in globals().items()
                           if (isinstance(value, (type, types.ClassType)) and
                               issubclass(value, unittest.TestCase))]
                               
    loader = unittest.TestLoader()
    big_suite = unittest.TestSuite(loader.loadTestsFromTestCase(test_class) 
                                   for test_class in test_classes_to_run)
                                   
    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)
