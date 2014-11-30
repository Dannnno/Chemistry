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
    from collections import deque
    import json
    import types
    
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
        self.atoms = atoms
        self.bonds = bonds
        self._add_nodes_from_(atoms)
        self._add_edges_from_(bonds)
        self.other_info = other_info
        
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
            
    def path(self, atoms, bonds=[]):
        if bonds:
            return self._path(atoms, bonds)
        first = self._get_first(atoms[0])
        paths = []
        for start in first:
            temp = self._get_path(start, atoms[1:])
            if temp:
                paths.append(temp)
        return set(self._flatten_tuples(self._get_tuples(paths)))
            
    def _get_tuples(self, mixed_list):
        """This function is necessary because there appears to be a bug
        in my path-finding algorithm, sometimes I get lists when I don't
        want them.  Once I find and fix that this'll be removed
        """
        tup = deque()
        if isinstance(mixed_list, (list, deque, tuple)):
            for t in mixed_list:
                if t:
                    if isinstance(t, (list, deque)):
                        tup.extendleft(self._get_tuples(t))
                    else:
                        tup.appendleft(t)
        return tup
        
    def _flatten_tuples(self, tuple_):
        """This function is necessary because I can't figure out why my
        tuples are becoming nested
        """
        if len(tuple_) == 1:
            return tuple(self._flatten_tuples(tuple_[0]))
        else: 
            tup = deque()
            for item in tuple_:
                if isinstance(item, tuple):
                    tup.append(self._flatten_tuples(item))
                else:
                    tup.append(item)
            return tuple(tup)
        
    def _path(self, atoms, bonds):
        if not all(isinstance(bond, (dict, types.NoneType)) for bond in bonds):
            raise TypeError("All information in bonds must be a NoneType or a dict")
        first = self._get_first(atoms[0])
        paths = []
        for start in first:
            temp = self._get_path_with_bond(start, atoms[1:], bonds)
            if temp:
                paths.append(temp)
        return set(self._flatten_tuples(self._get_tuples(paths)))
            
    def _get_path(self, starting_point, rest, so_far=()):
        so_far += (starting_point,)
        
        next_atom = self._get_next(starting_point, so_far, rest[0])
        
        if len(rest) == 1:
            return tuple(so_far + (atom,) for atom in next_atom)
        else:
            ret_tuples = map(lambda x: 
                                       self._get_path(x, 
                                                      rest[1:],
                                                      so_far),
                                   next_atom)
                                   
            return ret_tuples
            
    def _get_path_with_bond(self, starting_point, rest, bonds, so_far=()):
        so_far += (starting_point,)
        
        next_atom = self._get_next_with_bond(starting_point, so_far, bonds[0], rest[0])
        
        
        if len(rest) == 1:
            return tuple(so_far + (atom,) for atom in next_atom)
        else:
            ret_tuples = map(lambda x:
                                self._get_path_with_bond(x, 
                                                         rest[1:], 
                                                         bonds[1:],
                                                         so_far),
                             next_atom)
                             
            return ret_tuples
            
            
        if rest:
            paths = deque()
            super_paths = deque()
            for atom in starting_point:
                paths.append(self._join_paths(
                                so_far,
                                (atom,) + self._get_next_with_bond(
                                                atom,
                                                so_far + (atom,),
                                                bond=bonds[0],
                                                next_=rest[0])))
                                                
            for path in paths:
                super_paths.append(self._get_paths_with_bonds(
                                    (path[-1],), rest[1:], bonds[1:], path))
            return super_paths
        else:
            return so_far
            
    def _join_paths(self, first, second):
        if first:
            if first[-1] == second[0]:
                return first[:-1] + second
            else:
                return first + second
        else:
            return second
        
    def _get_first(self, atom):
        return [key 
                 for key, value in self.atoms.iteritems() 
                 if value == atom]
    
    def _get_next(self, atom, visited, next_=None):
        return self._filter_next(self._next_(atom), visited, next_=next_)
        
    def _get_next_with_bond(self, atom, visited, bond, next_=None):
        if bond is None:
            return self._get_next(atom, visited, next_)
        else:
            possible_neighbors = self._filter_next(self._next_(atom),
                                                   visited,
                                                   next_)
            valid_neighbors = ()
            for neighbor in possible_neighbors:
                info = self.edge[atom][neighbor].items()
                if all(data in info for data in bond.iteritems()):
                    valid_neighbors += (neighbor,)
            return valid_neighbors
                
    def _next_(self, atom):
        try:
            return self.neighbors(atom)
        except nx.exception.NetworkXError:
            raise KeyError("{} not in the graph".format(atom))
        
    def _filter_next(self, neighbors, visited, next_=None):
        return tuple(neighbor 
                      for neighbor in neighbors 
                      if neighbor not in visited and
                         ((next_ is not None and 
                           self.atoms[neighbor] == next_) or
                          (next_ is None)))
            
    def __contains__(self, key):
        if key in periodic_table:
            return key in self.atoms.values()
        elif key[0] in ['a', 'b']:
            try:
                int(key[1:])
            except TypeError:
                raise KeyError("Key {} not applicable".format(key))
            else:
                return key in self.atoms or key in self.bonds
                

if __name__ == '__main__':
    a = Compound({'a1':'H', 'a2':'O', 'a3':'C', 'a4':'C'}, 
                 {'b1':('a1', 'a2', {'order':1, 'chirality':None}), 
                  'b2':('a2', 'a3', {'order':1, 'chirality':None}),
                  'b3':('a3', 'a4', {'order':1, 'chirality':None})})
    print a.path(('H', 'O', 'C'), bonds=[{'order':1,'chirality':None},
                                          {'order':1,'chirality':None}])
    print
    b = Compound({'a1':'H', 'a2':'H', 'a3':'O'},
                 {'b1':('a1', 'a3', {'order':1, 'chirality':None}), 
                  'b2':('a2', 'a3', {'order':1, 'chirality':None})})
    print b.path(('H', 'O'), bonds=[{'order':1,'chirality':None}])