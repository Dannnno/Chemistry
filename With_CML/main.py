import csv
from copy import deepcopy
from collections import deque
from collections import OrderedDict
import sys
import pka
sys.path.insert(0, "C:/Users/Dan/Desktop/Programming/GitHub/Chemistry")
from CheML import CheML


hydronium = {"atoms": {
                       "a1": "H",
                       "a2": "H",
                       "a3": "H",
                       "a4": "O"
                      },
             "bonds": {
                       "b1": ("a1", "a4", 1),
                       "b2": ("a2", "a4", 1),
                       "b3": ("a3", "a4", 1)
                      }
            }

hydroxide = {"atoms": {
                       "a1": "H",
                       "a2": "O"
                      },
             "bonds": {
                       "b1": ("a1", "a2", 1)
                      }
            }

water = {"atoms": {
                   "a1": "H",
                   "a2": "H",
                   "a3": "O"
                  },
         "bonds": {
                   "b1": ("a1", "a3", 1),
                   "b2": ("a2", "a3", 1)
                  }
        }
        
carb_acid = {"atoms": {
                       "a1": "H",
                       "a2": "H",
                       "a3": "H",
                       "a4": "H",
                       "a5": "C",
                       "a6": "C",
                       "a7": "O",
                       "a8": "O"
                      },
             "bonds": {
                       "b1": ("a1", "a5", 1),
                       "b2": ("a2", "a5", 1),
                       "b3": ("a3", "a5", 1),
                       "b4": ("a5", "a6", 1),
                       "b5": ("a6", "a7", 1),
                       "b6": ("a4", "a7", 1),
                       "b7": ("a6", "a8", 2),
                      }
            }                      

# This variable is used for the Compound.getPKa() method.  It uses some common
# PKa patterns to assign approximate PKas to various molecules.  There will also 
# be program logic to work on an unknown compound, eventually
pka_patterns = pka.pka_patterns

def read_periodic_table():
    """Reads a csv file that represents all elements and pertinant data regarding
    them and then returns them as an OrderedDict
    """

    per_table = OrderedDict()
    with open("element_list.csv", "r") as f:
        my_reader = csv.reader(f)
        my_reader.next() # skips the header
        try:
            while True:
                tl = my_reader.next()
                # maps the desired types to the string counterparts
                col_types = [int, str, str, int, float, float, float,
                             float, float, float, float, str_to_list]
                new_row = tuple(convert_type(cell, typ)
                                for cell, typ in zip(tl, col_types))
                per_table[tl[1]] = new_row

        except StopIteration: # In case for some reason I need more elements..
            return per_table


periodic_table = read_periodic_table() # Populates a 'periodic table' 
                                       # that contains all the pertinent 
                                       # data for creating elements


def convert_type(cell, typ):
    """Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Takes a string and a function that the string should be represented as,
    if possible.  If the function can't be applied to that string then it returns
    "No_Data"
    """

    try:
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data" # The nomiker I have chosen for missing data


def str_to_list(a_stringy_list):
    """Takes a string that looks like a list and makes it a list
    Usage:
        >>>str_to_list("[1, 2, 3]") -> ["1", "2", "3"]
    """
    
    return a_stringy_list[1:-1].split(",")


def str_print_list(alist):
    """Prints a list using str() instead of repr()"""
    print "["+", ".join(map(str, alist))+"]"


def ret_str_list(alist):
    """Returns a str() of a list, not a repr()"""
    return "["+", ".join(map(str, alist))+"]"


def str_print_dict(adict):
    """Prints a dictionary using str() instead of repr()"""
    print "{"
    for key, value in adict.items():
        if isinstance(value, list) or isinstance(value, tuple):
            print " %s: %s," % (key, ret_str_list(value))
        else:
            print " %s: %s," % (key, value)
    print "}"


class Element(object):

    def __init__(self, symbol='C'):
        """Creates an Element object based on its symbol, assumed to be 'C'.
        """
        try:
            self.symbol = symbol
            self.number = periodic_table[symbol][0]
            self.name = periodic_table[symbol][2]
            self.group = periodic_table[symbol][3] # Find a better way to represent this
            self.weight = periodic_table[symbol][4]
            self.density = periodic_table[symbol][5]
            self.mp = periodic_table[symbol][6]
            self.bp = periodic_table[symbol][7]
            self.eneg = periodic_table[symbol][9]
            self.radius = periodic_table[symbol][10]
            self.oxid = periodic_table[symbol][11]
            self.bonds = []
            self.ismetal = False # Work out a way to do this
            self.root = 0
            self.check_root()
            
        except KeyError as e:
            print e

    def add_bond(self, other, bond_info):
        """Adds a bond to self and then to the other node"""
        try:
            if isinstance(other, Element):
                # bond_info is a tuple of varying size, depending on the 
                # specificity of bond object.  Contains a number of kwargs
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
        
        else:
            self.check_root() # Revalues the element's value as a 'root' node

    def remove_bond(self, bond):
        """Removes a bond from self and from other node"""
        try:
            if bond in self.bonds:
                if self == bond.first:
                    self.bonds.pop(bond)
                    bond.second.remove_bond(bond)
                elif self == bond.second:
                    bond.first.remove_bond(bond)
                    self.bonds.pop(bond)
                else:
                    raise BondingException(''.join(["Bond \"", repr(bond),
                                                "\" does not exist for element ",
                                                self.name]))
            else:
                raise BondingException(''.join(["Bond \"", repr(bond),
                                                "\" does not exist for element ",
                                                self.name]))
        except BondingException as BE:
            print BE
            return
            
        else:
            self.check_root() # Revalues the element's value as a 'root' node
            
    def check_root(self):
        """Function that determines how many 'children' the node (element) can
        have.  Double/Triple bonds are considered as well.  Electronegativity is
        taken into account elsewhere
        """

        self.root = 0
        for bond in self.bonds:
            self.root += int(bond.order)

    def __str__(self):
        return self.name

    def __repr__(self):
        return ''.join(["Element %s bonded to " % self.name,
                         ret_str_list([bond.get_other(self)
                                       for bond in self.bonds])])


class Bond(object):

    def __init__(self, first_element, second_element,
                 order=1, chirality="flat"):
        """Creates a bond object with various information, most of which is
        assumed
        """
        self.first = first_element
        self.second = second_element
        self.order = order
        self.chirality = chirality
        self.type = self.eval_bond() # Cleaner to do it this way imo

    def get_other(self, atom):
        """Method that determines the second node in a bond after being provided 
        with the other
        """
        if self.first == atom:
            return self.second
        elif self.second == atom:
            return self.first
        else:
            raise BondingException("Provided atom %s was not in the bond" %
                                    repr(atom))

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
        """Creates a molecule representation based on the input structured
        based on CheML.CMLParser()'s output
        """
        # I create deep copies because I'm not sure if I want to be able to 
        # safely mutate the originals or not
        self.atoms = deepcopy(mole_dict["atoms"])
        self.bonds = deepcopy(mole_dict["bonds"])
        self.walkable = OrderedDict() # A more crawler friendly structure
                                      # Look into a better way to do this

        for key, atom in self.atoms.iteritems(): # iterator uses less memory
            self.atoms[key] = Element(atom)

        for key, bond_info in self.bonds.items(): # mutating the dict, can't
                                                   # use the iterator
            atom1 = bond_info[0]
            atom2 = bond_info[1]
            order = bond_info[2]
            self.atoms[atom1].add_bond(self.atoms[atom2], (order,))
            self.bonds[(atom1, atom2)] = self.atoms[atom1].bonds[-1]
            del self.bonds[key] # Removing the old bond

        self.build_walkable() # Some semi complex logic, cleaner to create in
                              # a method
                              
        ## str_print_dict(self.walkable)
        ## print self.walkable

        self.pka = (100, "") 
        ## self.getPKa()     # getPKa(self) ?

    def build_walkable(self):
        """Builds a version of self.atoms that can be traversed by the
        Compound.walk() method
        """

        self.walkable["root"] = [self.atoms[self.getRoot()]]

        visited = set()
        to_crawl = deque(["root"])

        while to_crawl: # while there are still things to crawl
            current = to_crawl.popleft() # take the oldest

            if current in visited: # no cycle
                continue

            if current not in self.walkable.keys(): # Adds it if:
                                                     # 1. Other node is not in
                                                     #    the current nodes
                                                     # 2. It isn't the root 
                                                     #  ... I think I can get rid of that part
                self.walkable[current] = [bond.get_other(current)
                                          for bond in current.bonds
                                           if
                                            (bond.get_other(current) not in
                                             self.walkable.keys())
                                           and
                                            (bond.get_other(current) !=
                                             self.walkable["root"][0])
                                         ]

            visited.add(current)
            node_children = set(self.walkable[current])
            to_crawl.extend(node_children - visited) # rappends new options

    def walk(self, start=None):
        """Credit for the majority of this function goes to
        http://kmkeen.com/python-trees/2009-05-30-22-46-46-011.html
        """

        # logic is largely the same as self.build_walkable()
        
        if start is None:
            start = self.walkable["root"]
        elif start in self.walkable.keys():
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

        visited = list(visited)
        visited.insert(0, start)
        return visited

    def getPKa(self):
        """Determines the approximate PKa of the most acidic hydrogen in the 
        molecule.  Returns a tuple of form (pka_value, atom_id).  Relies on some
        fuzzy comparisons and will need constants tweaked
        """
        
        hydrogens = [hyd 
                     for hyd in self.walkable.keys() 
                      if (isinstance(hyd, Element) and 
                          hyd.name == "Hydrogen")
                    ]
        ## str_print_list(hydrogens)
        pka = 1000
        h_id = self.getID(hydrogens[0])
        threshold = 0
        for name, pattern in pka_patterns.items():
            # runs a fuzzy comparison on each hydrogen to the pattern
            # constants will need tweaking, as will implementation
            comparison = fuzzy_comparison(self.walkable, hydrogens, pattern)
            if comparison[0] > threshold:
                if comparison[0] == 1:
                    return (comparison[1], self.getID(hyd))
                pka = comparison[1]
                h_id = self.getID(hyd)
                threshold = comparison[0]
        return (pka, h_id)

    def getID(self, element):
        """Returns the id of an atom in a molecule"""
        for key, value in self.atoms.iteritems():
            if element == value:
                return key
        raise AttributeError("No such element in the compound")

    def getRoot(self):
        """Determines the most appropriate 'root' molecule based on the number
        and order of their bonds, and secondly by their electronegativities in 
        the case of a tie
        """
        
        # Just assumes the first one is a good choice
        most = sorted(self.atoms.keys())[0].root
        stored = [sorted(self.atoms.keys())[0]]
        for key, value in self.atoms.items():
            if value.root > most:
                most = value.root
                stored = [key]
            elif value.root == most:
                stored.append(key)

        most = self.atoms[stored[0]].eneg
        if isinstance(most, basestring):
            most = 0
        estored = stored[0]

        # Checks for electronegativity
        for key in stored:
            if isinstance(self.atoms[key].eneg, basestring):
                continue # This only happens if there is "No_Data"
            if self.atoms[key].eneg > most:
                most = self.atoms[key].eneg
                estored = key

        return estored

    def __str__(self):
        return str(self.atoms) + str(self.bonds)

    def __repr__(self):
        return repr(self.atoms) + repr(self.bonds)


class BondingException(Exception):

    def __init__(self, err_message="Bonding Error"):
        """An exception to be used when a bonding error occurs.  A more 
        descriptive error message is encouraged
        """
        self.err_message = err_message

    def __str__(self):
        return self.err_message

    def __repr__(self):
        return self.err_message


class ReactionException(Exception):

    def __init__(self, err_message="Reaction Error"):
        """An exception to be used when a reaction error occurs.  A more 
        descriptive error message is encouraged
        """
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

    # I have no idea what I'm doing here
    # This should be ignored until I have an effective way to locate the two
    # different key sites
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
    """Removes a proton from a compound (acid) and then recalculates its pka"""
    
    # This will eventually have stuff that actually removes a proton
    acid.pka = acid.getPKa()  # Has to be reset after the changes occur


def add_proton(base):
    """Adds a proton to a compound (base) and then recalculates its pka"""
    
    # This will eventually have stuff that actually adds a proton
    base.pka = base.getPKa()
    
    
def fuzzy_comparison(walkable, hydrogens, pattern):
    """This method takes a walkable compound dictionary, a dictionary of
    available hydrogens, and a pka_pattern to compare to.  Runs a fuzzy comparison
    based on some constants that are tbd
    """
    
    ## str_print_dict(walkable)
    # heh.  Gives me a hydrogen first look
    elbaklaw = walk_reverse(walkable, hydrogens) 
    str_print_dict(elbaklaw) 
    for key, connected_to in walkable.iteritems(): 
        pass # Doesn't do anything yet~
    return (0, 1000) # Just some nonsense values


def walk_reverse(walkable, hydrogens):
    """This method takes a walkable dictionary and a list of hydrogens, and then
    reverse the orientation of the walkable dictionary such that hydrogens
    are first
    """

    # Logic is basically the same as Compound.build_walkable()    
    reverse_walkable = OrderedDict()
    
    visited = set()
    to_crawl = deque(hydrogens)
    
    while to_crawl:
        current = to_crawl.popleft()
        
        if current in visited:
            continue

        if current not in reverse_walkable:
            reverse_walkable[current] = [bond.get_other(current)
                                         for bond in current.bonds
                                         if
                                         (bond.get_other(current) not in
                                         reverse_walkable.keys())
                                        ]
        visited.add(current)
        node_children = set(reverse_walkable[current])
        to_crawl.extend(node_children - visited)
    
    return reverse_walkable

if __name__ == "__main__":
    """Main body of the program.  Creates some of the molecules and pka patterns
    and gets everything set up to actually react some stuff.  Full of testing 
    stuff, will be cleaner and probably in a function, eventually
    """
    
    molecules = {''.join(['m', str(i)]): molecule 
                 for i, molecule in 
                 enumerate([hydronium, hydroxide, water, carb_acid])
                } # Just the molecules I have ready for testing purposes
                
    length = len(molecules)

    # Making some cml files for funsies.  Will be
    # removed when I'm sure the CML stuff won't change
    for key in molecules.keys(): 
        CheML.CMLBuilder(molecules[key], key, ''.join([key, ".cml"]))

    molecules = OrderedDict() # Reassings this name! But its okay, it'll use
                              # the same data, just a nicer format for me
    for filename in [''.join(['m', str(i), ".cml"]) for i in range(length)]:
        mole = CheML.CMLParser(filename) # Parsing those files I made above
        molecules[mole.id] = mole.molecule
    
    # Setting the pka values for my predetermined values
    for mol_pka, molecule, h_id in pka_patterns.values(): 
        molecule = Compound(molecule)
        mol_pka = (molecule.pka, h_id)
        
    ## compounds = map(Compound, molecules.values())
    comp = Compound(molecules["m3"]) # Just using one of them for now
    comp.getPKa() # Testing my pka stuff
    ## str_print_dict(comp.walkable)
    ## str_print_list(ac.walk())

    ## acid_base_rxn(acid=hydronium, base=hydroxide, a=ad, b=bd, c=md)
