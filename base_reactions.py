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

from copy import deepcopy
import abc

import numpy as np

import compounds
import periodic_table as pt
periodic_table = pt.periodic_table


class Reactant(object):
    
    @classmethod
    def _compare_pkas(cls, acid_pka, base_pka, thresholds={}):
        if thresholds:
            raise NotImplementedError
        else:
            pass
        
    @classmethod
    def make_Base(cls, basic_compound, pka=16, point='a1'):
        if isinstance(basic_compound, Base):
            return basic_compound
        else:
            try:
                return Base(basic_compound, 16, 'a1')
            except Exception as e:
                print e
        
    @classmethod
    def make_Acid(cls, acidic_compound, pka=16, point='a1'):
        if isinstance(acidic_compound, Acid):
            return acidic_compound
        else:
            try:
                return Acid(acidic_compound, 16, 'a1')
            except Exception as e:
                print e
        
    @classmethod
    def _new_key(cls, compound, atom=True):
        if atom:
            max_key = max(compound.atoms)
            letter = 'a'
        else:
            max_key = max(compound.bonds)
            letter = 'b'
        number = int(max_key[1:])+1
        return "{}{}".format(letter, number)

    def __init__(self, compound, paths={}):
        self._Compound = compound
        self.paths = dict() # { key: set() }
        if paths:
            self.add_paths(**paths)
        
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
            
    def _validate_pka(self, pka):
        try:
            self.__dict__['pka']
        except KeyError:
            self.pka = pka
        else:
            if pka != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))
                
    def __getattr__(self, attr):
        return getattr(self._Compound, attr)  
        
    def __eq__(self, other):
        try:
            return self._Compound == other._Compound
        except AttributeError:
            return self._Compound == other
        
    def __ne__(self, other):
        return not self == other
        
    def __len__(self):
        return len(self._Compound)
        
    def __getitem__(self, key):
        return self._Compound.__getitem__(key)
            
            
class Acid(Reactant):

    def __init__(self, compound, acidic_point, pka, paths={}):
        super(Acid, self).__init__(compound, paths)
        self.acidic_point = acidic_point
        self._validate_pka(pka)   
        
                
class Base(Reactant):

    def __init__(self, compound, basic_point, pka, paths={}):
        """The pka of a Base should be equal to that of its conjugate
        acid
        """
        
        super(Base, self).__init__(compound, paths)
        self.conjugate = None
        self.conjugate_acid = None
        self.basic_point = basic_point
        self._validate_pka(pka)  
        self.to_conjugate_Acid()
        
    def to_conjugate_Acid(self):
        self.conjugate = deepcopy(self._Compound)
        a_key = Reactant._new_key(self.conjugate)
        b_key = Reactant._new_key(self.conjugate, False)
        hydrogen = compounds.get_Element('H')
        self.conjugate._add_node_(a_key, hydrogen)
        self.conjugate._add_edge_(b_key, a_key, self.basic_point)
        self.conjugate_acid = Acid(self.conjugate, a_key, self.pka, self.paths)        
        

class Product(object): 
    
    def __init__(self, compound, percentage, all_percentages):
        self._Compound = compound
        self.paths = dict() # { key: set() }
        self.major = (True 
                      if percentage >= np.mean(all_percentages) 
                      else False) 
        self.percentage = percentage
        
    def __getattr__(self, attr):
        return getattr(self._Compound, attr)


class Conditions(object): 
    
    def __init__(self, **conditions):
        self.__dict__.update(conditions)

    def has_reactants(self):
        return 'reactants' in self and self.reactants
        
    def validate_reactants(self, *reactants):
        if self.has_reactants():
            return all(reactant in self.reactants for reactant in reactants)   
        else:
            return False
        
    def add_reactants(self, *reactants):
        if self.has_reactants():
            self.reactants.extend(reactants)
        else:
            self.reactants = reactants   
                        
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
        

class ReactionError(Exception):
    err_message = "There was an error with the reaction"
    pka = """
    AcidBase reaction between {} and {} failed because of pka difference {}
    ({} to {})    
    """
    
    def __init__(self, *args, **kwargs):
        if 'pka' in kwargs:
            self.err_message = ReactionError.pka.format(*kwargs['reactants']
                                                        *kwargs['pka'])
            
    def __str__(self):
        return self.err_message
        
    def __repr__(self):
        return str(self)
            
        

if __name__ == '__main__':
    pass
    