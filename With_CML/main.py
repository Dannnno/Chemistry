import csv
# import os
# from collections import deque # look into this for tree walking
# import networkx # look into this for a graph approach
# os.chdir("C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry")
# print os.listdir(os.getcwd())
# from CheML import CMLParser


hydronium = {"atoms" : { 
                        "a1" : "H",
                        "a2" : "H",
                        "a3" : "H",
                        "a4" : "O" 
                       },
             "bonds" : {
                        "b1" : ("a1", "a4", 1),
                        "b2" : ("a2", "a4", 1),
                        "b3" : ("a3", "a4", 1)
                       }
             }
                
hydroxide = {"atoms" : { 
                        "a1" : "H",
                        "a2" : "O" 
                       },
             "bonds" : {
                        "b1" : ("a1", "a2", 1)
                       }
            }       


def read_periodic_table(): 
    per_table = {}
    with open("element_list.csv", "r") as f:
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
        self.group = periodic_table[symbol][3] # Find a better way to do this
        self.weight = periodic_table[symbol][4]
        self.density = periodic_table[symbol][5]
        self.mp = periodic_table[symbol][6]
        self.bp = periodic_table[symbol][7]
        self.eneg = periodic_table[symbol][9]
        self.radius = periodic_table[symbol][10]
        self.oxid = periodic_table[symbol][11]
        self.bonds = []
        self.ismetal = False # Work out a way to do this
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
        """This method will determine covalent/ionic bond
        Uses http://www.chemteam.info/Bonding/Electroneg-Bond-Polarity.html
        for the boundaries between types
        """
        
        delta = abs(self.first.eneg - self.second.eneg)
        if delta <= 0.5:
            return "Non-polar covalent"
        elif delta <= 1.6 or (delta <= 2 and not (self.first.ismetal or 
                                                   self.second.ismetal)):
            return "Polar-covalent"
        elif delta > 2 or (delta <= 2 and (self.first.ismetal or 
                                            self.second.ismetal)):
            return "Ionic"
        else:
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
            
        self.pka = self.getPKa()
            
        
    def walk(self, start=None, parameters=None): 
        if parameters is None:
            raise ReactionException("No search parameters defined")
        if start is None:
            start = sorted(self.atoms.keys)[0]

    
    def getPKa(self): return 0
    
    
    def __str__(self):
        return str(self.atoms) + str(self.bonds)
        

    def __repr__(self):
        return repr(self.atoms) + repr(self.bonds)


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


def acid_base_rxn(acid=hydronium, base=hydroxide, aqueous=True, **kwargs): 
    """Used to simulate acid-base reactions.  Assumes an aqueous environment
    unless otherwise indicated.  If not reacting in water additional keyword
    arguments should be provided
    """
    
    for k,v in kwargs.iteritems():
        print k, v
        
    if not kwargs:
        a_pka = acid.pka
        b_pka = base.pka
        if a_pka > b_pka:
            a_pka, b_pka, acid, base = b_pka, a_pka, base, acid
        remove_proton(acid)
        add_proton(base)
        a_pka = acid.pka
        b_pka = base.pka
        
        if b_pka - a_pka < 1:
            acid_base_rxn(acid, base, aqueous, **kwargs)
            
def remove_proton(acid): pass
def add_proton(base): pass

if __name__ == "__main__":
    periodic_table = read_periodic_table()
    ad = {"a1" : "H", "a2" : "H", "a3" : "O"}
    bd = {"b1" : ("a1", "a3", 1), "b2" : ("a2", "a3", 1)}
    md = {"atoms" : ad, "bonds" : bd}
    ac = Compound(md) 
                
    acid_base_rxn(acid=hydronium, base=hydroxide, a=ad, b=bd, c=md)                            
    
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
    