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
import json

from lxml import etree
from lxml import builder as lb
              
          
class CMLParser(object):
    
    def __init__(self, CML_file):
        """Should be given an open file"""
        self.CML_file = CML_file
        self.bonds = {}
        self.atoms = {}
        self.other = {}
        self.molecule = {'atoms': self.atoms, 
                         'bonds': self.bonds, 
                         'other_info': self.other}
        
        self.CML_tree = etree.iterparse(self.CML_file)
        atom, bond = True, False
        last = ''
        
        for _, element in self.CML_tree:
            if element.tag == 'molecule':
                self.other.update(dict(element.items()))
                
            elif element.tag == 'atomArray':
                atom, bond = False, True
                last = []
                
            elif atom:
                if 'string' in element.tag:
                    last = element.text
                elif 'atom' in element.tag:
                    self.atoms[element.get('id')] = last
                    
            elif bond:
                if 'string' in element.tag:
                    last.append(element.text)
                elif 'bond' in element.tag:
                    self.bonds[element.get('id')] = [part for part in last]
                    last = []
                    
        del self.bonds[None]
        
        for key, bond in self.bonds.items():
            try:
                rest = bond[2:]
            except KeyError:
                self.bonds[key] = (bond[0], bond[1], 
                                   {'order': 1, 'chirality': 'None'},)
            else:
                if len(rest) == 1:
                    self.bonds[key] = (bond[0], bond[1], 
                                       {'order': int(rest[0]), 
                                        'chirality': 'None'})
                elif len(rest) == 2:
                    self.bonds[key] = (bond[0], bond[1], 
                                       {'order': int(rest[0]),
                                        'chirality': rest[1]})
                else:
                    d = {'order': int(rest[0]),
                         'chirality': rest[1]}
                    i=0
                    for value in rest[2:]:
                        d['unknown{}'.format(i)] = '{}'.format(value)
                        i+=1
                    self.bonds[key] = (bond[0], bond[1], d)
            if self.bonds[key][2]['chirality'] == 'None':
                self.bonds[key][2]['chirality'] = None
                    
            
    def __str__(self):
        return json.dumps(self.molecule, indent=4)
            
    
class CMLBuilder(object):
    
    @classmethod
    def from_Compound(cls, comp):
        comp = deepcopy(comp)
        atoms = comp.atoms
        bonds = {}
        
        for bkey, bdata in comp.bonds.iteritems():
            bonds.update({bkey: (bdata[0], bdata[1], 
                                {'order': str(bdata[2]['order']),
                                 'chirality': str(bdata[2]['chirality'])})})
            
        other = {key:str(value) for key, value in comp.other_info.iteritems()}
        m = {'atoms': atoms, 'bonds': bonds, 'other_info': other}
        return CMLBuilder(m)
        
    def __init__(self, molecule_dict):
        self.atoms = molecule_dict['atoms']
        self.bonds = molecule_dict['bonds']
        self.attribs = molecule_dict['other_info']
        
        for key, atom in self.atoms.items():
            self.atoms[key] = lb.E.atom(lb.E.string(atom, 
                                                    builtin="elementType"), 
                                        id=key)
            
        for key, bond in self.bonds.items():
            order = str(bond[2]['order'])
            chirality = str(bond[2]['chirality'])
            self.bonds[key] = lb.E.bond(
                                lb.E.string(bond[0], builtin="atomRef"),
                                lb.E.string(bond[1], builtin="atomRef"),
                                lb.E.string(order, builtin="order"),
                                lb.E.string(chirality, builtin="chirality"),
                                id=key)                                                                                                               
 
        self.CML = lb.E.molecule(
                        lb.E.atomArray(*sorted(self.atoms.values(),
                                               key=lambda x:x.get('id'))),
                        lb.E.bondArray(*sorted(self.bonds.values(),
                                               key=lambda x:x.get('id'))),
                        **self.attribs)
                        
    def to_file(self, cml_file):
        """Should be given an open file"""
        try:
            cml_file.write(str(self))
        except AttributeError:
            raise TypeError(''.join(
                                      ["to_file() should be given an ",
                                       "open file-like object, not a {}"]
                                     ).format(type(cml_file)))
        
    def __str__(self):
        return etree.tostring(self.CML, pretty_print=True) 
        
    def __repr__(self):
        return str(self)
        
    
if __name__ == '__main__':
    import os
    
    with open(os.getcwd() + "/molecules/test_molecules/CML_1.cml", 'r') as f:
        print CMLParser(f)