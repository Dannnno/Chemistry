"""from __future__ import print_function

class foo():
    def __str__(self):
        return "String"
    def __repr__(self):
        return "Repr"

print([foo()])

def my_decorator(func):
    def inner(alist):
        if isinstance(alist, list):
            return func("["+", ".join(map(str, alist))+"]")
        else:
            return func(alist)
    return inner

print = my_decorator(print)
print([foo()])
"""

import csv
from copy import deepcopy
from collections import deque
from collections import OrderedDict
import sys
sys.path.insert(0, "C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry")
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
                       "a2": "O",
                       "a3": "C",
                       "a4": "O",
                       "a5": "H"
                      },
             "bonds": {
                       "b1": ("a1", "a2", 1),
                       "b2": ("a2", "a3", 1),
                       "b3": ("a3", "a4", 2),
                       "b4": ("a3", "a5", 1)
                      }
            }                      

# This variable is used for the Compound.getPKa() method.  It uses some common
# PKa patterns to assign approximate PKas to various molecules.  There will also 
# be program logic to work on an unknown compound, eventually
pka_patterns = OrderedDict()
pka_patterns["Alkane"] = ("RCH3", 50)
pka_patterns["Alkene"] = ("")
pka_patterns = {"Alcohol": ("RCOH", 0),
                "Carboxylic Acid": ("RCOOH", 0),
                
               }

def read_periodic_table():
    """Reads a csv file that represents all elements and pertinant data regarding
    them and then returns them as an OrderedDict
    """

    per_table = OrderedDict()
    with open("element_list.csv", "r") as f:
        my_reader = csv.reader(f)
        my_reader.next()
        try:
            while True:
                tl = my_reader.next()
                col_types = [int, str, str, int, float, float, float,
                             float, float, float, float, str_to_list]
                new_row = tuple(convert_type(cell, typ)
                                for cell, typ in zip(tl, col_types))
                per_table[tl[1]] = new_row

        except StopIteration:
            return per_table


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
        return "No_Data"


def str_to_list(a_stringy_list):
    return a_stringy_list[1:-1].split(",")


"""class MyStdOut(object):

    def __init__(self, term=sys.stdout):
        self.out = term

    def write(self, text):
        try:
            a = text.split()
            if a[0] == "Element":
                self.out.write(a[1])
            elif a[0] == "Bond":
                self.out.write(text)
            elif a[1] == "bond":
                self.out.write("Bond between %s and %s" % (a[3], a[5]))
            else:
                self.out.write(text)
        except IndexError:
            self.out.write(text)
        #self.out.write("String\n" + str(text) +
        #               "\nRepr\n" + repr(text) +
        #               "\nDefault\n" + text + "\n")

sys.stdout = MyStdOut()
"""

def str_print_list(alist):
    print "["+", ".join(map(str, alist))+"]"


def ret_str_list(alist):
    return "["+", ".join(map(str, alist))+"]"


def str_print_dict(adict):
    print "{"
    for key, value in adict.items():
        if isinstance(value, list) or isinstance(value, tuple):
            print " %s: %s," % (key, ret_str_list(value))
        else:
            print " %s: %s," % (key, value)
    print "}"


class Element(object):

    def __init__(self, symbol='C'):
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Element %s bonded to " % self.name + ret_str_list([bond.get_other(self) for bond in self.bonds])


class Bond(object):

    def __init__(self, first_element, second_element,
                 order=1, chirality="flat"):
        self.first = first_element
        self.second = second_element
        self.order = order
        self.chirality = chirality
        self.type = self.eval_bond()

    def get_other(self, atom):
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
            self.bonds[(atom1, atom2)] = self.atoms[atom1].bonds[-1]
            del self.bonds[key]

        self.build_walkable()
        str_print_dict(self.walkable)
        self.pka = self.getPKa() # getPKa(self) ?
        # print self.walkable

    def build_walkable(self):
        """Builds a version of self.atoms that can be traversed by the
        Compound.walk() method
        """

        self.walkable = OrderedDict()
        self.walkable["root"] = [self.atoms[self.getRoot()]]

        visited = set()
        to_crawl = deque(["root"])

        while to_crawl:
            current = to_crawl.popleft()

            if current in visited:
                continue

            if current not in self.walkable.keys():
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
            to_crawl.extend(node_children - visited)

    def walk(self, start=None):
        """Credit for the majority of this function goes to
        http://kmkeen.com/python-trees/2009-05-30-22-46-46-011.html
        """

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
        hydrogens = [hyd 
                     for hyd in self.walkable.keys() 
                      if (isinstance(hyd, Element) and 
                          hyd.name == "Hydrogen")
                    ]
        str_print_list(hydrogens)
        for hyd in hydrogens:
            print repr(hyd)
        for name, pattern in pka_patterns.items():
            print name, pattern
        return 0

    def getRoot(self):
        most = 0
        stored = [sorted(self.atoms.keys())[0]]
        for key, value in self.atoms.items():
            if len(value.bonds) > most:
                most = len(value.bonds)
                stored = [key]
            elif len(value.bonds) == most:
                stored.append(key)

        most = self.atoms[stored[0]].eneg
        estored = stored[0]

        for key in stored:
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

    acid.pka = acid.getPKa()  # Has to be reset after the changes occur


def add_proton(base):

    base.pka = base.getPKa()


if __name__ == "__main__":
    molecules = {''.join(['m', str(i)]): molecule for i, molecule in enumerate([hydronium, hydroxide, water, carb_acid])}
    length = len(molecules)

    for key in molecules.keys():
        CheML.CMLBuilder(molecules[key], key, ''.join([key, ".cml"]))

    molecules = OrderedDict()
    for filename in [''.join(['m', str(i), ".cml"]) for i in range(length)]:
        mole = CheML.CMLParser(filename)
        molecules[mole.id] = mole.molecule
    periodic_table = read_periodic_table()
    # compounds = map(Compound, molecules.values())
    comp = Compound(molecules["m3"])
    # str_print_list(ac.walk())

    # acid_base_rxn(acid=hydronium, base=hydroxide, a=ad, b=bd, c=md)
