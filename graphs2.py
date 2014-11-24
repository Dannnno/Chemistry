from collections import OrderedDict
from functools import total_ordering
from periodic_table import periodic_table
import itertools


class Graph(object):
    
    def __init__(self, atoms, bonds, other_info={}):
        self.atoms = OrderedDict(sorted((
                                         (key,Element(value))
                                         for key, value in atoms.iteritems()
                                        ),
                                        key=lambda x: (x[1], x[0])))
        self.bonds = OrderedDict(sorted((
                                         (key, Bond(self.atoms[value[0]], 
                                                    self.atoms[value[1]], 
                                                    value[2]))
                                         for key, value in bonds.iteritems()
                                        ),
                                        key=lambda x: (x[1], x[0])))
        self.molecule = {'atoms':self.atoms, 'bonds':self.bonds}
        self.other_info = other_info
        
class CompoundTree(Graph):
    
    def __init__(self, atoms, bonds, other_info={}, connections={}):
        super(CompoundTree, self).__init__(atoms, bonds, other_info)
        
        
class CompoundRing(Graph):
    
    def __init__(self, atoms, bonds, other_info={}, connections={}):
        super(CompoundRing, self).__init__(atoms, bonds, other_info)
        
class SubGraphConnectors(Graph):
    
    def __init__(self, graph1, graph2, atoms, bonds, other_info={}):
        super(SubGraphConnectors, self).__init__(atoms, bonds, other_info)
        self.graph1, self.graph2 = graph1, graph2
        self.left_graph, self.right_graph = [], []
        for key, bond in self.bonds.iteritems():
            self.left_graph.append(bond.first)
            self.right_graph.append(bond.second)
            
        lval = self.graph1.atoms.values()
        rval = self.graph2.atoms.values()
        for left, right in itertools.izip(self.left_graph, self.right_graph):
            if not (left in lval and right in rval):
                raise ValueError(
                    "All left values must in in graph1 and right values graph2")
                    
        
            
                                                   
        
        
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
        self.is_metal = False ## Figure out how to do this
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
                "The order of a bond must be [1,2,3], not {}".format(order))
        if chirality not in [None, 'R', 'S', 'E', 'Z']:
            raise ValueError(''.join(["A bond must have no ",
                                        "(None) chirality or R/S/E/Z ",
                                        "chirality, not {}"]).format(chirality))
        if element1 is element2:
            raise ValueError("A bond can't go from an element to itself.")
            
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
        elif delta <= 1.6 or (delta <= 2 and not (self.first.is_metal or
                                                   self.second.is_metal)):
            self.type = "Polar-covalent"
        elif delta > 2 or (delta <= 2 and (self.first.is_metal or
                                            self.second.is_metal)):
            self.type = "Ionic"
        else:
            self.type = "Unknown type" 
            
    def __getitem__(self, i):
        if i in [0, 'first']:
            return self.first
        elif i in [1, 'second']:
            return self.second
        else:
            raise IndexError("There are only two items in a bond")
            
    def __contains__(self, element):
        ## I need to consider how strict I want this to be - do I want
        ## an is-element or an equals-element requirement?
        return (element == self[0]) or (element == self[1])        
        
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
    g1 = CompoundTree({"a1":"H", "a2":"H", "a3":"O"},
                         {"b1":("a1", "a3", 1), 
                          "b2":("a2", "a3", 1)},
                         {"id":"Water"})
    g2 = CompoundTree({"a1":"H", "a2":"H", "a3":"O"},
                         {"b1":("a1", "a3", 1), 
                          "b2":("a2", "a3", 1)},
                         {"id":"Water"})
    SubGraphConnectors(g1, g2, {"a1":"H", "a2":"H", "a3":"O",
                        "a4":"H", "a5":"H", "a6":"O"},
                         {"b1":("a1", "a4", 1), 
                          "b2":("a2", "a5", 1),
                          "b3":("a3", "a6", 2)})