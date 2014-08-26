import csv
from collections import deque # look into this for tree walking
import networkx # look into this for a graph approach


def read_periodic_table(): 
    per_table = {}
    with open("element_list.txt", "r") as f:
        my_reader = csv.reader(f)
        my_reader.next()
        try:
            while True:
                tl = my_reader.next()
                col_types = [int, str, str, int, float, float, float, float, float, float, float, str_to_list]
                new_row = tuple(convert_type(cell, typ) for cell, typ in zip(tl, col_types))
                per_table[tl[1]] = new_row
                
        except StopIteration:
            return per_table


def convert_type(cell, typ):
    """Credit to SO user Marius for this function
    http://stackoverflow.com/a/25498445/3076272
    """
    
    try:
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data"


def str_to_list(a_stringy_list):
    a_stringy_list[1:-1].split(",")


class Element(object):
    #count = [0]*118

    def __init__(self, symbol='C'):
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
        self.bonds = []
        #Element.count[number] += 1

    def add_bond(self, other, bond_info):
        try:
            if isinstance(other, Element):
                temp_bond = Bond(self, other, *bond_info)
                self.bonds.append(temp_bond)
                other.bonds.append(temp_bond)

            else:
                raise BondingException(''.join(["Object \"", repr(other), "\":",
                                                str(type(other)), " could not",
                                                " be bonded to element ",
                                                self.name]))
        except BondingException as BE:
            print BE
            return

    def remove_bond(self, bond):
        try:
            if bond in self.bonds:
                self.bonds.pop(bond)
            else:
                raise BondingException(''.join(["Bond \"", repr(bond),
                                                "\" does not exist for element ",
                                                self.name]))
        except BondingException as BE:
            print BE
            return
            
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return "Element %s bonded to " % self.name + str(self.bonds)

    def __del__(self):
        #Element.count[self.number] += -1
        pass


class Bond(object):

    def __init__(self, first_element, first_ref, second_element, 
                 second_ref, order=1, chirality="flat"):
        self.first = first_element
        self.fref = first_ref
        self.second = second_element
        self.sref = second_ref
        self.order = order
        self.chirality = chirality
        self.type = self.eval_bond()

    def eval_bond(self):
        """This method will (eventually) determine covalent/ionic bond"""
        return "Unknown type"
        
        
    def __str__(self):
        return "Bond between %s and %s" % (self.first.name, self.second.name)

        
    def __repr__(self):
        return "%s bond between %s and %s of order %d and chirality %s)" \
                % (self.type, self.first.name, self.second.name, 
                   self.order, self.chirality)


class Compound(object):
    
    def __init__(self, mole_dict):
        self.atoms = mole_dict["atoms"] # Consider making a new copy with dict()
        self.bonds = mole_dict["bonds"]
        
        for atom in self.atoms:
            self.atoms[atom] = Element(self.atoms[atom])
          
        for bond in self.bonds:
            self.bonds[bond] = (self.atoms[self.bonds[bond][0]],
                                self.bonds[bond][0],
                                self.atoms[self.bonds[bond][1]],
                                self.bonds[bond][1],
                                self.bonds[bond][2])
            self.bonds[bond] = Bond(*self.bonds[bond])
            
    def __str__(self):
        return str(self.atoms) + str(self.bonds)
        
    def __repr__(self):
        return repr(self.atoms) + repr(self.bonds)
        
    def walk(self, start=None, parameters=None): 
        if parameters is None:
            raise ReactionException("No search parameters defined")
        if start is None:
            start = sorted(self.atoms.keys)[0]


class BondingException(Exception):

    def __init__(self, err_message="Bonding Error"):
        self.err_message = err_message

    def __str__(self):
        return self.err_message

    def __repr__(self):
        return self.err_message


class ReactionException(Exception):
    
    def __init__(self, err_message="Reaction Error"):
        self.err_message = err_message
        
    def __str__(self):
        return self.err_message

    def __repr__(self):
        return self.err_message


if __name__ == "__main__":
    periodic_table = read_periodic_table()
    ad = {"a1" : "H", "a2" : "H", "a3" : "O"}
    bd = {"b1" : ("a1", "a3", 1), "b2" : ("a2", "a3", 1)}
    md = {"atoms" : ad, "bonds" : bd}
    ac = Compound(md)
    
    """
    #print Element.count[12]
    a = Element("C")
    print a
    #print Element.count[12]
    b = Element()
    print b
    #print Element.count[12]
    del a
    #print Element.count[12]
    del b
    #print Element.count[12]
    """
    