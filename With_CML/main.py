from copy import deepcopy
from collections import deque
from collections import OrderedDict
import sys
import pka
import time
import csv
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

# This variable is used for the Compound.get_PKa() method.  It uses some common
# PKa patterns to assign approximate PKas to various molecules.  There will also
# be program logic to work on an unknown compound, eventually
pka_patterns = pka.pka_patterns


def time_decorator(my_function):
    """ This is a decorator I use to test how long my different functions take.
    Hopefully I can use this to determine which method of checking is ideal

    By which method I mean either:
        1. Hardcoding how to scan a molecule's hydrogens and use some algorithm
           to assign a pka value (or range)
        2. Compare everything to my predetermined pka pattern/values and then
           assign a pka based on similarity
    """

    def inner(*args, **kwargs):
        start = time.time()
        return_value = my_function(*args, **kwargs)
        end = time.time()
        print "%s executed in %.2f seconds\n" % (my_function.__name__, end-start)
        return return_value
    return inner

def convert_type(cell, typ):
    """Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Takes a string and a function that the string should be represented as,
    if possible.  If the function can't be applied to that string then it returns
    "No_Data"
    """

    try:
        if typ == str_to_list:
            return typ(cell, mapped=int)
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data" # The nomiker I have chosen for missing data


def str_to_list(a_stringy_list, mapped=None):
    """Takes a string that looks like a list and makes it a list
    Usage:
        >>> str_to_list("[1, 2, 3]")
        ["1", "2", "3"]
    If mapped is provided a function it will map that function to the list
    """
    the_list = a_stringy_list[1:-1].split(",")
    try:
        # Fun fact, mapping 'None' to a list just returns the list
        return map(mapped, the_list)
    except ValueError: #Exception:
        ## print "Function %s couldn't be mapped to list " % str(mapped), the_list
        return the_list


def str_print_list(alist):
    """Prints a list using str() instead of repr()"""
    print "["+", ".join(map(str, alist))+"]"


def ret_str_list(alist):
    """Returns a str() of a list, not a repr()"""
    return "["+", ".join(map(str, alist))+"]"


#def str_print_dict(adict):
#    """Prints a dictionary using str() instead of repr()"""
#    print "{"
#    if "root" in adict:
#        print "root: %s" % ret_str_list(adict["root"])
#        s_keys = sorted(adict.keys(), key=lambda x: x.root if not x == "root" else "root")
#        print s_keys
#        for item in s_keys:
#            if item != "root":
#                print "%s: %s" % (item.name, ret_str_list(adict[item]))
#    else:
#        for key, value in adict.items():
#            if isinstance(value, list) or isinstance(value, tuple):
#                print " %s: %s," % (key, ret_str_list(value))
#            else:
#                print " %s: %s," % (key, value)
#    print "}"


def str_print_dict(adict):
    """Prints a dictionary using str() instead of repr()"""
    print "{"
    for key, value in adict.items():
        if isinstance(value, list) or isinstance(value, tuple):
            print " %s: %s," % (key, ret_str_list(value))
        else:
            print " %s: %s," % (key, value)
    print "}"


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


def get_pka(hydrogen):
    if hydrogen.bonds:
        other = hydrogen.bonds[0].get_other(hydrogen)
        if other.name == "Carbon":
            if len(other.bonds) == 4:
                ## print "SP3 Carbon"
                return 50.
            elif len(other.bonds) == 3:
                if other.root == 4:
                    ## print "SP2 Carbon"
                    return 44.
                str_print_list(other.bonds)
                print len(other.bonds), other.root
                for bond in other.bonds:
                    print bond, bond.order
                raise NotImplementedError("Carbon Ion")
            elif len(other.bonds) == 2:
                if other.root == 4:
                    ## print "SP Carbon"
                    return 25.
                raise NotImplementedError("Carbon Ion")
        elif other.name == "Nitrogen":
            if len(other.bonds) == 4:
                ## print "Positive Nitrogen"
                return 9.2
            elif len(other.bonds) == 3:
                ## print "Amine"
                return 38.
            raise NotImplementedError("Nitrogen problem")
        elif other.name == "Hydrogen":
            ## print "Conjugate acid of H-"
            return 35.
        elif other.name == "Sulfur":
            if len(other.bonds) == 2:
                ## print "Thiol"
                return 7.
            raise NotImplementedError("Sulfur problem")
        elif other.name == "Chlorine":
            ## print "Hydrochloric acid"
            return -6.
        elif other.name == "Bromine":
            ## print "Hydrobromic acid"
            return -9.
        elif other.name == "Iodine":
            ## print "Hydroiodic acid"
            return -10.
        elif other.name == "Oxygen":
            # Things get hairy
            if len(other.bonds) == 3:
                ## print "Positive Oxygen"
                return -2.
            elif len(other.bonds) == 2:
                next_other = other.bonds[0].get_other(other)
                next_name = next_other.name
                if next_name == "Carbon":
                    if next_other.is_aromatic:
                        print "Phenol"
                        raise NotImplementedError("Aromatic system")
                    elif len(next_other.bonds) == 4:
                        ## print "Alcohol"
                        return 16.
                    elif next_other.root == 4:
                        for bond in next_other.bonds:
                            next_next = bond.get_other(next_other)
                            if (next_next.name == "Oxygen" and
                            bond.order == 2):
                                continue
                            if next_next.name == "Carbon":
                                if any((abond.get_other(next_next).eneg > 2.5)
                                       for abond in next_next.bonds):
                                       print "Carboxylic acid with eneg groups"
                                       return 0.2
                                else:
                                    print "Carboxylic acid"
                                    return 4.8
                            raise NotImplementedError("What is happening here")
                elif next_name == "Hydrogen":
                    ## print "Water"
                    return 15.7
                elif next_name == "Sulfur":
                    ## print "Sulfuric acid"
                    return -9.
            elif other.root == 3:
                print "Protonated diene system"
                raise NotImplementedError("Protonated diene")
        raise NotImplementedError("Nothing matches")
    else:
        raise NotImplementedError("This hydrogen isn't bonded to anything")


#class Memoize:
#    """Taken from http://stackoverflow.com/a/1988826/3076272"""
#
#    def __init__(self, f):
#        self.f = f
#        self.memo = {}
#    def __call__(self, *args, **kwargs):
#        print args, type(args)
#        print kwargs
#        if kwargs:
#            if not (str(args), str(kwargs)) in self.memo:
#                self.memo[(str(args), str(kwargs))] = self.f(*args, **kwargs)
#        else:
#            if not str(args) in self.memo:
#                self.memo[str(args)] = self.f(*args)
#
#        return self.memo[str(args)]


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
            self.root = 0
            self.check_root()

            # Work out a way to do these
            self.ismetal = False
            self.is_aromatic = False

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
        acc = 0
        for bond in self.bonds:
            acc += bond.order
        self.root = acc

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
        return ''.join(["Element %s bonded to " % self.name,
                         ret_str_list([bond.get_other(self)
                                       for bond in self.bonds])])

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

class Bond(object):

    def __init__(self, first_element, second_element,
                 order=1, chirality="flat"):
        """Creates a bond object with various information, most of which is
        assumed
        """
        self.first = first_element
        self.second = second_element
        self.order = int(order)
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
        return str(self)
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
        self.depth = 0

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

        # Some more complex logic, decided it makes more sense to do methods
        self.root = self.get_root()
        self.build_walkable()
        self.depth = self.get_depth()
        self.pka = (100, "")
        ## self.get_PKa()

    def build_walkable(self):
        """Builds a version of self.atoms that can be traversed by the
        Compound.walk() method

        Doesn't handle cycles or rings
        """

        self.walkable = walk_compound(self.atoms[self.root], root=True)
        self.depth = self.get_depth()

    def get_depth(self, key=None, depth=1):
        """Gets the depth of the walkable dictionary"""
        self.depth = 0

        if key is None:
            return self.get_depth(key=self.walkable["root"][0])
        else:
            try:
                return max(self.get_depth(key=element, depth=depth+1) for element in self.walkable[key])
            except ValueError:
                return depth

    def get_PKa(self):
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
        # threshold = 0
        self.pka = (min(map(get_pka, hydrogens) + [pka]), h_id)
        #for name, pattern in pka_patterns.items():
        #    # runs a fuzzy comparison on each hydrogen to the pattern
        #    # constants will need tweaking, as will implementation
        #    comparison = fuzzy_comparison(self.walkable, hydrogens, pattern)
        #    if comparison[0] > threshold:
        #        if comparison[0] == 1:
        #            return (comparison[1], self.getID(hyd))
        #        pka = comparison[1]
        #        h_id = self.getID(hyd)
        #        threshold = comparison[0]
        #    break
        #return (pka, h_id)

    def getID(self, element):
        """Returns the id of an atom in a molecule"""
        for key, value in self.atoms.iteritems():
            if element == value:
                return key
        raise AttributeError("No such element in the compound")

    def get_root(self):
        """Determines the most appropriate 'root' molecule based on the number
        and order of their bonds, and secondly by their electronegativities in
        the case of a tie
        """

        # Just assumes the first one is a good choice
        most = self.atoms[sorted(self.atoms.keys())[0]].root
        stored = [sorted(self.atoms.keys())[0]]
        for key, value in self.atoms.items():
            if value.root > most:
                most = value.root
                stored = [key]
            elif value.root == most:
                stored.append(key)

        most = self.atoms[stored[0]].eneg
        if isinstance(most, basestring):
            most = 0      # This only happens if there is "No_Data"
        estored = stored[0]

        # Checks for electronegativity
        for key in stored:
            if isinstance(self.atoms[key].eneg, basestring):
                continue       # This only happens if there is "No_Data"
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
    acid.pka = acid.get_PKa()  # Has to be reset after the changes occur


def add_proton(base):
    """Adds a proton to a compound (base) and then recalculates its pka"""

    # This will eventually have stuff that actually adds a proton
    base.pka = base.get_PKa()


def fuzzy_comparison(walkable, hydrogens, pattern):
    """This method takes a walkable compound dictionary, a dictionary of
    available hydrogens, and a pka_pattern to compare to.  Runs a fuzzy comparison
    based on some constants that are tbd

    No idea how I'm doing this at the moment
    """

    # This gives me a walkable compound rooted at the acidic proton
    str_print_dict(walkable)
    target = walk_compound(pattern[1].atoms[pattern[2]], root=True)
    str_print_dict(target)
    # heh.  Gives me a hydrogen first look
    elbaklaw = walk_compound(hydrogens)
    str_print_dict(elbaklaw)
    for key, connected_to in walkable.iteritems():
        pass # Doesn't do anything yet~
    return (0, 1000) # Just some nonsense values


# fuzzy_comparison = Memoize(fuzzy_comparison)


def walk_compound(start, root=False):
    walkable = {}

    visited = set()
    if isinstance(start, list):
        to_crawl = deque(start)
    elif not root:
        to_crawl = deque([start])
    else:
        to_crawl = deque([start])
        walkable["root"] = [start]

    while to_crawl:
        current = to_crawl.popleft()

        if current in visited:
            continue
        if current not in walkable:
            walkable[current] = [bond.get_other(current)
                                  for bond in current.bonds
                                   if (bond.get_other(current) not in
                                   walkable.keys())
                                ]

        visited.add(current)
        node_children = set(walkable[current])
        to_crawl.extend(node_children - visited)

    return walkable


# walk_compound = Memoize(walk_compound)


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
    for key, (mol_pka, molecule, h_id) in pka_patterns.items():
        try:
            molecule = Compound(molecule)
            molecule.get_PKa()
            molecule.pka = (mol_pka, h_id)
            pka_patterns[key] = (mol_pka, molecule, h_id)
            # print molecule.pka
        except NotImplementedError as e:
            print key,": issue with", e
            str_print_dict(molecule.walkable)
            pass

    ## compounds = map(Compound, molecules.values())
    ## comp = Compound(molecules["m3"]) # Just using one of them for now
    ## str_print_dict(comp.walkable) # comp
    ## get_pka = time_decorator(get_pka)
    ## print comp.pka
    # This (mostly) correctly outputs the different hydrogens
    # SP3 Carbon
    # get_pka executed in 0.00 seconds
    #
    # SP3 Carbon
    # get_pka executed in 0.00 seconds
    #
    # SP3 Carbon
    # get_pka executed in 0.00 seconds
    #
    # Carboxylic acid with eneg groups
    # This is wrong. We should see that this is a normal Carboxylic acid
    # get_pka executed in 0.00 seconds
    #
    # (0.2, "a1")
