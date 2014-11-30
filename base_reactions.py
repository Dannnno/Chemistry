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

import numpy as np

import compounds
import periodic_table as pt
periodic_table = pt.periodic_table


class Reactant(compounds.Compound): 

    def __init__(self, atoms, bonds, other_info={}):
        super(Reactant, self).__init__(atoms, bonds, other_info)
        self.paths = dict() # { key: set() }
        
    def add_paths(self, **paths):
        for reaction, path in paths.iteritems():
            if reaction in self.paths:
                self.paths[reaction].add(path)
            else:
                self.paths[reaction] = set([path])
                
    def get_paths(self, reaction):
        try:
            return self.paths[reaction]
        except KeyError:
            raise KeyError("{} paths haven't been found yet".format(reaction))
            
            
class Acid(Reactant):

    def __init__(self, atoms, bonds, acidic_point, pka, other_info={}):
        super(Acid, self).__init__(atoms, bonds, other_info)
        self.acidic_point = acidic_point
        self._validate_pka()
                
    def _validate_pka(self, pka):
        try:
            self.__dict__['pka']
        except KeyError:
            self.pka = pka
        else:
            if pka != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))
        
            
class Base(Reactant):
    
    def __init__(self, atoms, bonds, basic_point, pka, other_info={}):
        self.basic_point = basic_point
        self._validate_pka()
                
    def _validate_pka(self, pka):
        try:
            self.__dict__['pka']
        except KeyError:
            self.pka = pka
        else:
            if pka != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))


class Product(compounds.Compound): 
    
    def __init__(self, atoms, bonds, percentage, all_percentages, other_info={}):
        super(Product, self).__init__(atoms, bonds, other_info)
        self.paths = dict() # { key: set() }
        self.major = (True 
                      if percentage >= np.mean(all_percentages) 
                      else False) 
        self.percentage = percentage


class Conditions(object): 
    
    def __init__(self, **conditions):
        self.__dict__.update(conditions)

    def has_reactants(self):
        return 'reactants' in self and self['reactants']     
        
    def add_reactants(self, reactants):
        if self.has_reactants():
            self['reactants'].extend(reactants)
        else:
            self['reactants'] = reactants   
                        
    def __getitem__(self, key):
        return self.__dict__[key]
        
    def __contains__(self, key):
        return key in self.__dict__


class Reaction(object):
    paths = dict()
    
    @classmethod
    def _parse_reactants(cls, *reactants):
        pass
        
    @abc.abstractmethod
    def _eval_paths(self):
        pass
        
    @abc.abstractmethod
    def react(self):
        pass
        

if __name__ == '__main__':
    pass