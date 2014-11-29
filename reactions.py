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

import abc

import compound_graphs as cg


class Reaction(object):
    _paths = frozenset()
    
    def __init__(self, *reactants, **conditions):
        self.reactants, self.conditions = reactants, conditions
        i=0
        for reactant in reactants:
            self.__dict__['reactant{}'.format(i)] = reactant
            i += 1
        for condition, setting in conditions.iteritems():
            self.__dict__[condition] = setting
            
    @classmethod
    @abc.abstractproperty
    def _get_paths(cls):
        return cls._paths
            
    @abc.abstractmethod
    def react(self): pass
        
    @abc.abstractmethod
    def _find_paths(self): pass
        
        
class AcidBase(Reaction):
    
    def __init__(self, *reactants, **conditions): 
        super(AcidBase, self).__init__(*reactants, **conditions)
        for reactant in self.reactants:
            print reactant
    
    
if __name__ == '__main__':
    compound1 = cg.Compound({"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                     {"b1":("a1", "a3", 1), 
                                      "b2":("a2", "a3", 1),
                                      "b3":("a3", "a4", 1)},
                                     {"id":"Hydronium"})
    compound2 = cg.Compound({"a1": "H", "a2": "O"},
                                     {"b1": ("a1", "a2", 1)},
                                     {"id":"Hydroxide"})
    AcidBase(compound1, compound2)