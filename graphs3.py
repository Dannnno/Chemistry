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
    from periodic_table2 import periodic_table
    import periodic_table2 as pt
except ImportError:
    import table_builder2
    table_builder2.build_table()
    del globals()['table_builder2']
    from periodic_table2 import periodic_table
    import periodic_table2 as pt
finally:
    import json
    
    import networkx as nx
    
    import CheML2 as cml

def get_Element(symbol='C'):
    return {"symbol":symbol} #periodic_table[symbol]


class Compound(nx.Graph):

    @classmethod
    def from_CML(cls, CML_file):        
        try:
            with open(CML_file, 'r') as CML_in:
                parsed = cml.CMLParser(CML_in)
        except TypeError:
            parsed = cml.CMLParser(CML_file)
        return Compound(parsed.atoms,
                         parsed.bonds,
                         {key: value
                          for key, value in parsed.molecule.iteritems()
                          if key not in ["atoms", "bonds"]})
   
    def __init__(self, atoms, bonds, other_info={}):
        super(Compound, self).__init__()
        self._add_nodes_from_(atoms)
        self._add_edges_from_(bonds)
        
    def _add_nodes_from_(self, atoms):
        for key, atom in atoms.iteritems():
            self._add_node_(key, get_Element(atom))
        
    def _add_edges_from_(self, bonds):
        for id_, bond in bonds.iteritems():
            self._add_edge_(id_, *bond)
            
    def _add_node_(self, key, atom):
        try:
            self.node[key]
        except KeyError:
            self.add_node(key, **atom)
        else:
            raise KeyError("There is already an atom {}".format(key))
            
    def _add_edge_(self, key, first, second, rest):
        try:
            self.edge[first][second]
        except KeyError:            
            d = {'order':1, 'chirality':None}
            d.update(rest)
            self.add_edge(first, second, key=key, **d)
        else:
            raise KeyError("There is already a bond {}".format(key))
        

if __name__ == '__main__':
    a = Compound({'a1':'H', 'a2':'H', 'a3':'O'}, 
                 {'b1':('a1', 'a2', {'order':1, 'chirality':None}), 
                  'b2':('a2', 'a3', {'order':1, 'chirality':None})})
    print a.__dict__