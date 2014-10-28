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

from collections import OrderedDict
from functools import partial
from functools import total_ordering
import csv
import json
import os

import CheML2 as cml
    
    
## My global functions
        
def convert_type(cell, typ):
    """Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Takes a string and a function that the string should be represented as,
    if possible.  
    
    For example,
    >>> convert_type('4', int)
    4
    >>> convert_type('4.0', float)
    4.0
    >>> convert_type('[1,2,3]', str_to_list)
    [1, 2, 3]
    
    If the function can't be applied to that string then it returns
    "No_Data"
    >>> convert_type('No Data', int)
    'No_Data'
    """

    try:
        if typ is str_to_list:
            return typ(cell, mapped=int)
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data" # The nomiker I have chosen for missing data
        
def str_to_list(a_stringy_list, mapped=None):
    """Takes a string that looks like a list and makes it a list
    
    >>> str_to_list("[1,2,3]")
    ['1', '2', '3']
    
    If a function to be mapped is provided it will attempt to do so
    >>> str_to_list("[1,2,3]", mapped=int)
    [1, 2, 3]
    """
    
    the_list = a_stringy_list[1:-1].split(",")
    try:
        # Fun fact, mapping 'None' to a list just returns the list
        return map(mapped, the_list)
    except ValueError: #Exception:
        ## print "Function %s couldn't be mapped to list " % str(mapped), the_list
        return the_list
        
def read_periodic_table(filename):
    """Reads a csv file that represents all elements and pertinant data regarding
    them and then returns them as an OrderedDict
    """

    per_table = OrderedDict()
    
    with open(filename, "r") as f:
        my_reader = csv.reader(f)
        my_reader.next() # skips the header
        for i in range(118):
            tl = my_reader.next()
            col_types = [int, str, str, int, float, float, float,
                         float, float, float, float, str_to_list]
            new_row = tuple(convert_type(cell, typ)
                            for cell, typ in zip(tl, col_types))
            per_table[tl[1]] = new_row
    
    return per_table
    
# Populates my periodic table with all of the element data
try:
    # For some reason it needs the rest of the path when I run this, but it 
    # doesn't when I run the unit tests...
    periodic_table = read_periodic_table(os.getcwd()+"/desktop/programming/github/chemistry/element_list.csv") 
except IOError:
    periodic_table = read_periodic_table(os.getcwd()+"/element_list.csv") 


class Compound(object): 
    
    @classmethod
    def from_CML(cls, CML_file):
        """An alternate constructor if I'd like to load this directly from a 
        CML file
        
        #>>> Compound.from_CML(os.getcwd() + 
        #...                   "/molecules/test_molecules/CML_1.cml") == \\
        #...       Compound({"a1":"H", "a2":"H", "a3":"O"},
        #...                {"b1":("a1", "a3", 1), 
        #...                 "b2":("a2", "a3", 1)})
        #True
        """
        with open(CML_file, 'r') as CML_in:
            parsed = cml.CMLParser(CML_in)
        return Compound(parsed.atoms, 
                         parsed.bonds, 
                         {key:value 
                          for key, value in parsed.molecule.iteritems()
                          if key not in ["atoms", "bonds"]})
        
    @classmethod
    def json_serialize(cls, obj, as_str=False):
        """Serializes a compound (or ay other) object for json,
        and is then used to make a detailed and pretty repr of a Compound instance
        
        >>> a, b = Element(), Element()                        
        >>> Compound.json_serialize(Bond(a, b))  == \\
        ...            {'second': b, 'first': a, 'chirality': None, 
        ...             'order': 1, 'type': 'Non-polar covalent',
        ...             'bond': set([a, b])}
        True
         
        >>> Compound.json_serialize(set([1, 2, 3]))
        ['1', '2', '3']
        """
        
        if as_str:
            d = {}
            
            if isinstance(obj, Element):
                for key, value in obj.__dict__.iteritems():
                    if key == 'name':
                        d[key] = value
                    elif key == 'bonded_to':
                        d[key] = map(str, value)
                        
            elif isinstance(obj, Bond):
                for key, value in obj.__dict__.iteritems():
                    if key in ['first', 'second']:
                        d[key] = str(value)
                        
            elif isinstance(obj, Compound):
                d.update(obj.__dict__)
                
            else:
                try:
                    return obj.__dict__
                except AttributeError:
                    return map(repr, obj)
                    
            return d          
        else:
            try:
                return obj.__dict__
            except AttributeError:
                return map(repr, obj)

    def __init__(self, atoms, bonds, other_info):
        self.atoms = OrderedDict(sorted((
                                         (key,Element(value))
                                         for key, value in atoms.iteritems()
                                        ),
                                        key=lambda x: (x[1], x[0])))
        self.bonds = OrderedDict(sorted((
                                         (key, Bond(self[value[0]], 
                                                    self[value[1]], 
                                                    value[2]))
                                         for key, value in bonds.iteritems()
                                        ),
                                        key=lambda x: (x[1], x[0])))
        self.molecule = {'atoms':self.atoms, 'bonds':self.bonds}
        self.molecule.update(other_info)
        self.root = None
        self.get_root()
        
    def get_root(self):
        """Gets the root of a molecule.  Does so by evaluating the 'root'
        value of each non-Hydrogen atom
        
        >>> comp = Compound({"a1":"O", "a2":"H", "a3":"H"},
        ...                 {"b1":("a1", "a2", 1), 
        ...                  "b2":("a1", "a3", 1)},
        ...                 {})
        >>> comp.root is comp['a1']
        True
        """
        
        root_val = -1
        root_eneg = self.atoms['a1'].eneg
        for atom in self.atoms.itervalues():
            if ((atom.symbol != 'H') and
                ((atom.root[0] > root_val) or 
                 (atom.root[0] == root_val and atom.root[1] > root_eneg))):
                root_val = atom.root[0]
                root_eneg = atom.root[1]
                self.root = atom
                
    def to_cml(self, filename):
        cml.CMLBuilder.from_Compound(self, filename)
            
    def __getitem__(self, i):
        if (not isinstance(i, basestring)) or (i[0] not in ['a', 'b']):
            raise KeyError(' '.join(["Keys must be strings of form a#",
                                       "or b#, where # is some number"]))
        elif i[0] == 'a':
            return self.atoms[i]
        else:
            return self.bonds[i]
            
    def __str__(self):
        return '\n'.join(map(partial(json.dumps,
                                      default=partial(self.json_serialize,
                                                      as_str=True),
                                      sort_keys=True,
                                      indent=4),
                              [self.atoms, self.bonds]))
                                      
    def __repr__(self):        
        return '\n'.join(map(partial(json.dumps,
                                      default=self.json_serialize,
                                      sort_keys=True, 
                                      indent=4),
                              [self.atoms, self.bonds]))
                              
    def __eq__(self,other):
        try:
            return all(getattr(self,key)==getattr(other,key)
                       for key in self.__dict__ if not key.startswith('_'))
        except AttributeError:
            return False
            
    def __ne__(self, other):
        return not self == other


@total_ordering
class Element(object): 

    def __init__(self, symbol='C'):
        self.bonds = set()
        self.bonded_to = set()

        self.symbol = symbol
        self.number = periodic_table[symbol][0]
        self.name = periodic_table[symbol][2]
        self.group = periodic_table[symbol][3] ## Better way of doing this
        self.weight = periodic_table[symbol][4]
        self.density = periodic_table[symbol][5]
        self.mp = periodic_table[symbol][6]
        self.bp = periodic_table[symbol][7]
        self.eneg = periodic_table[symbol][9]
        self.radius = periodic_table[symbol][10]
        self.oxid = periodic_table[symbol][11]
        self.ismetal = False ## Figure out how to do this
        self.root = (0, self.eneg)
        self.get_root()
        
    def create_bond(self, a_bond, an_element):
        """Adds a bond and the other element to self's sets"""
        self.bonds.add(a_bond)
        self.bonded_to.add(an_element)
        self.get_root()
        
    def break_bond(self, a_bond, flag=False):
        """Breaks (removes) a bond from self to other.  The flag variable
        ensures that we don't hit an infinitely recursive scenario
        
        >>> a, b = Element(), Element()
        >>> ab = Bond(a, b)
        >>> a.break_bond(ab)
        >>> ((ab not in a.bonds) and
        ...  (ab not in b.bonds) and
        ...  (a not in b.bonded_to) and
        ...  (b not in a.bonded_to))
        True
        """
        
        other = a_bond.get_other(self)
        self.bonds.discard(a_bond)
        self.bonded_to.discard(other)
        if not flag:
            other.break_bond(a_bond, True)
        self.get_root()
        
    def get_root(self):
        """Determines the 'root' value of an atom
        
        >>> a, b = Element(), Element()
        >>> a.get_root()
        >>> a.root == b.root == (0, a.eneg)
        True
        >>> ab = Bond(a, b)
        >>> a.root == b.root == (1, a.eneg)
        True
        >>> a.break_bond(ab)
        >>> a.root == b.root == (0, a.eneg)
        True
        """
        
        acc = 0
        for bond in self.bonds:
            if bond.get_other(self).symbol !='H':
                    acc += bond.order
        self.root = (acc, self.eneg)
        
    def __str__(self):
        return self.symbol
        
    def __repr__(self):
        return "Element {} bonded to {}".format(self.symbol, map(str, self.bonded_to))
        
    def __eq__(self, other):
        """These are very weak implementations of == and !="""
        return self.symbol == other.symbol
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __lt__(self, other):
        if self == other:
            return len(self.bonds) < len(other.bonds)
        else:
            return self.number < other.number


@total_ordering
class Bond(object): 

    def __init__(self, element1, element2, order=1, chirality=None):
        """Creates a bond object with the necessary information.  
        
        >>> a, b = Element(), Element()
        >>> ab = Bond(a, b)
        >>> ((ab.first == a) and
        ...  (ab.second == b) and
        ...  (ab.order == 1) and
        ...  (ab.chirality is None) and
        ...  (ab.type == 'Non-polar covalent'))
        True
        
        If the bond is given impossible situations (such as bond order > 4, 
        or an unknown chirality), a ValueError will be raised
        >>> try:
        ...     Bond(a, b, 4)        
        ... except ValueError:
        ...     print 'ValueError'
        ...     try:
        ...         Bond(a, b, 1, 'Q')        
        ...     except ValueError:
        ...         print 'ValueError'
        ...         try:
        ...             Bond(a, a)        
        ...         except ValueError:
        ...             print 'ValueError'
        ValueError
        ValueError
        ValueError
        """
        
        if int(order) not in xrange(1, 4):
            raise ValueError(
                "The order of a bond must be [1,3], not {}".format(order))
        if chirality not in [None, 'R', 'S', 'E', 'Z']:
            raise ValueError(''.join(["A bond must have no ",
                                        "(None) chirality or R/S/E/Z ",
                                        "chirality, not {}"]).format(chirality))
        if element1 is element2:
            raise ValueError("A bond can/'t go from an element to itself.")
            
        self.order = int(order)
        self.chirality = chirality
        self.bond = set([element1, element2])
        self.first = element1
        self.second = element2
        element1.create_bond(self, element2)
        element2.create_bond(self, element1)
        self.eval_bond()
        
    def get_other(self, an_element):
        """Gets the other element in a bond (ie the adjacent vertex)
        
        >>> a, b = Element('O'), Element('H')
        >>> ab = Bond(a, b)
        >>> ab.get_other(a)
        Element H bonded to ['O']
        >>> ab.get_other(b)
        Element O bonded to ['H']
        """
        
        if an_element in self.bond:
            if an_element is self.first:
                return self.second
            return self.first
        raise KeyError('Element {} not in bond {}'.format(an_element, self))
        
    def eval_bond(self):
        """This method will determine covalent/ionic bond
        Uses http://www.chemteam.info/Bonding/Electroneg-Bond-Polarity.html
        for the boundaries between types
        """

        delta = abs(self.first.eneg - self.second.eneg)
        if delta <= 0.5:
            self.type = "Non-polar covalent"
        elif delta <= 1.6 or (delta <= 2 and not (self.first.ismetal or
                                                   self.second.ismetal)):
            self.type = "Polar-covalent"
        elif delta > 2 or (delta <= 2 and (self.first.ismetal or
                                            self.second.ismetal)):
            self.type = "Ionic"
        else:
            self.type = "Unknown type" 
            
    def __getitem__(self, i):
        if i == 0:
            return self.first
        elif i == 1:
            return self.second
        else:
            raise IndexError("There are only two items in a bond")
        
    def __str__(self):
        return "Bond between {} and {}".format(self.first, self.second)
        
    def __repr__(self):
        return ' '.join(["Bond between {} and {} of:",
                          "order {},",
                          "chirality {}"]).format(self.first, 
                                                  self.second, 
                                                  self.order, 
                                                  self.chirality)
                                                  
    def __eq__(self, other):
        return ((self.order == other.order) and
                 ((self.first == other.first and self.second == other.second) or
                  (self.first == other.second and self.second == other.first)))
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __lt__(self, other):
        if self.order == other.order:
            for one, two in zip(sorted(self.bond), sorted(other.bond)):
                if one < two:
                    return True                    
        return self.order < other.order
     
     
if __name__ == '__main__':     
    pass
    