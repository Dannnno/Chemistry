import csv
from copy import deepcopy
from collections import deque # look into this for tree walking
import networkx # look into this for a graph approach


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

water = {"atoms" : { 
                    "a1" : "H",
                    "a2" : "H",
                    "a3" : "O" 
                   },
         "bonds" : {
                    "b1" : ("a1", "a3", 1),
                    "b2" : ("a2", "a3", 1)
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


class Bond(object):

    def __init__(self, first_element, second_element, 
                 order=1, chirality="flat"):
        self.first = first_element
        self.second = second_element
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
        return "%s bond between %s and %s of order %d with %s chirality" \
                % (self.type, self.first.name, self.second.name, 
                   self.order, self.chirality)


class Compound(object):
    
    def __init__(self, mole_dict):
        self.atoms = deepcopy(mole_dict["atoms"])
        self.bonds = deepcopy(mole_dict["bonds"])
        self.walkable = {}
        
        for key, atom in self.atoms.iteritems():
            self.atoms[key] = Element(atom)
        
        for key, bond_info in self.bonds.items():
            atom1 = bond_info[0]
            atom2 = bond_info[1]
            order = bond_info[2]
            self.atoms[atom1].add_bond(self.atoms[atom2], (order,))
            
            self.bonds[(atom1, atom2)] = Bond(self.atoms[atom1], 
                                              self.atoms[atom2],
                                              order)

            del self.bonds[key]
            
        self.pka = self.getPKa() # getPKa(self) ?
        
        self.walkable = self.build_walkable()
        print self.walkable
     
        
    def build_walkable(self):
        atom_keys= sorted(self.atoms.keys())
        self.walkable["root"] = [self.atoms[atom_keys[0]]]
        atoms = [self.atoms[key] for key in atom_keys]
        for atom in atoms:
            if atom not in self.walkable.keys():
                self.walkable[atom] = [bonded_to 
                                       for bonded_to in atom.bonds 
                                       if 
                                        (bonded_to not in self.walkable.keys()) 
                                        and 
                                         (bonded_to != self.walkable["root"][0])
                                      ]
              
    def walk(self, start=None): 
        """Credit for the majority of this function goes to
        http://kmkeen.com/python-trees/2009-05-30-22-46-46-011.html
        """
        
        if start is None:
            start = self.getRoot()
        elif start in self.walkable:
            pass
        else:
            raise ReactionException("Starting location not present in molecule")
            
        visited = set()
        to_crawl = deque([start])
            
        while to_crawl:
            current = to_crawl.popleft()
            if current in visited:
                continue
            visited.add(current)
            node_children = set(self.walkable[current])
            to_crawl.extend(node_children - visited)
        
        return list(visited)

    
    def getPKa(self): 
        return 0
        
    
    def getRoot(self): 
        return sorted(self.walkable["root"])
    
    
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


def getPKa(a_compound): 
    data = a_compound.walk()


def acid_base_rxn(acid=hydronium, base=hydroxide, aqueous=True, **kwargs): 
    """Used to simulate acid-base reactions.  Assumes an aqueous environment
    unless otherwise indicated.  If not reacting in water additional keyword
    arguments should be provided
    """
    
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

                        
def remove_proton(acid): 
    pass
    
    
def add_proton(base): 
    pass


if __name__ == "__main__":
    periodic_table = read_periodic_table()
    ad = {"a1" : "H", "a2" : "H", "a3" : "O"}
    bd = {"b1" : ("a1", "a3", 1), "b2" : ("a2", "a3", 1)}
    md = {"atoms" : ad, "bonds" : bd}
    ac = Compound(md) 
    print ac.walk()
                
    acid_base_rxn(acid=hydronium, base=hydroxide, a=ad, b=bd, c=md)                            
