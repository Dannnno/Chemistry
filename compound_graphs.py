from functools import partial
import json
        

class Compound(object): 

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
                              
    @classmethod
    def json_serialize(cls, obj):
        try:
            return obj.__dict__
        except AttributeError:
            return map(repr, obj)


class Element(object): 

    def __init__(self, symbol='C'):
        self.symbol = symbol
        self.bonds = set()
        self.bonded_to = set()
        
    def create_bond(self, a_bond, an_element):
        self.bonds.add(a_bond)
        self.bonded_to.add(an_element)
        
    def break_bond(self, a_bond):
        other = a_bond.get_other(self)
        self.bonds.discard(a_bond)
        self.bonded_to.discard(other)
        other.break_bond(a_bond)
        
    def __str__(self):
        return self.symbol
        
    def __repr__(self):
        return "Element {} bonded to {}".format(self.symbol, map(str, self.bonded_to))


class Bond(object): 

    def __init__(self, element1, element2, order=1, chirality=None):
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
                
a = Compound({'a1':'O', 'a2':'H', 'a3':'H'},
             {'b1':('a1', 'a2', 1), 'b2':('a1', 'a3', 1)})                
print a