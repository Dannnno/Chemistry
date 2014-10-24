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
import csv
import json
import os
    
    
## My global functions
        
def convert_type(cell, typ):
    """Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Takes a string and a function that the string should be represented as,
    if possible.  If the function can't be applied to that string then it returns
    "No_Data"
    """

    try:
        if typ is str_to_list:
            return typ(cell, mapped=int)
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data" # The nomiker I have chosen for missing data
        
def str_to_list(a_stringy_list, mapped=None):
    """Takes a string that looks like a list and makes it a list
    Usage:
        >>> str_to_list("[1, 2, 3]")
        ["1", "2", "3"]
    If mapped is provided a function it will map that function to the list
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
        """
        raise NotImplementedError
        
    @classmethod
    def json_serialize(cls, obj):
        try:
            return obj.__dict__
        except AttributeError:
            return map(repr, obj)

    def __init__(self, atoms, bonds):
        self.atoms = {key:Element(value) for key, value in atoms.iteritems()}
        for key, value in bonds.iteritems():
            bonds[key] = (self.atoms[value[0]], self.atoms[value[1]], value[2])
        self.bonds = {key:Bond(*value) for key, value in bonds.iteritems()}
                                      
    def __repr__(self):
        return '\n'.join(map(partial(json.dumps,
                                      default=self.json_serialize,
                                      sort_keys=True, 
                                      indent=4),
                              [self.atoms, self.bonds]))


class Element(object): 

    def __init__(self, symbol='C'):
        self.bonds = set()
        self.bonded_to = set()

        self.symbol = symbol
        self.number = periodic_table[symbol][0]
        self.name = periodic_table[symbol][2]
        self.group = periodic_table[symbol][3] 
        self.weight = periodic_table[symbol][4]
        self.density = periodic_table[symbol][5]
        self.mp = periodic_table[symbol][6]
        self.bp = periodic_table[symbol][7]
        self.eneg = periodic_table[symbol][9]
        self.radius = periodic_table[symbol][10]
        self.oxid = periodic_table[symbol][11]
        
        
    def create_bond(self, a_bond, an_element):
        self.bonds.add(a_bond)
        self.bonded_to.add(an_element)
        
    def break_bond(self, a_bond, flag=False):
        other = a_bond.get_other(self)
        self.bonds.discard(a_bond)
        self.bonded_to.discard(other)
        if not flag:
            other.break_bond(a_bond, True)
        
    def __str__(self):
        return self.symbol
        
    def __repr__(self):
        return "Element {} bonded to {}".format(self.symbol, map(str, self.bonded_to))


class Bond(object): 

    def __init__(self, element1, element2, order=1, chirality=None):
        if order not in xrange(1, 4):
            raise ValueError(
                "The order of a bond must be [1,3], not {}".format(order))
        if chirality not in [None, 'R', 'S', 'E', 'Z']:
            raise ValueError(''.join(["A bond must have no ",
                                        "(None) chirality or R/S/E/Z ",
                                        "chirality, not {}"]).format(chirality))
        self.order = order
        self.chirality = chirality
        self.bond = set([element1, element2])
        self.first = element1
        self.second = element2
        element1.create_bond(self, element2)
        element2.create_bond(self, element1)
        
    def get_other(self, an_element):
        if an_element in self.bond:
            for element in self.bond:
                if an_element is not element: return element
        raise KeyError('Element {} not in bond {}'.format(an_element, self))
        
    def __str__(self):
        return "Bond between {} and {}".format(self.first, self.second)
        
    def __repr__(self):
        return ' '.join(["Bond between {} and {} of:",
                          "order {},",
                          "chirality {}"]).format(self.first, 
                                                  self.second, 
                                                  self.order, 
                                                  self.chirality)
     
if __name__ == '__main__':           
    pass
