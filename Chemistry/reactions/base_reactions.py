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
import abc
import types

from Chemistry import compounds


class Reactant(object):

    @classmethod
    def _compare_pkas(cls, comp1, comp2, conditions=None, thresholds={}):
        raise NotImplementedError

    @classmethod
    def make_Base(cls, basic_compound, pka=16, point='a1'):
        if isinstance(basic_compound, Base):
            return basic_compound
        else:
            try:
                return Base(basic_compound, point, pka)
            except Exception as e:
                print e

    @classmethod
    def make_Acid(cls, acidic_compound, pka=16, point='a1'):
        if isinstance(acidic_compound, Acid):
            return acidic_compound
        else:
            try:
                return Acid(acidic_compound, point, pka)
            except Exception as e:
                print e

    @classmethod
    def _new_key(cls, compound, atom=True):
        if atom:
            max_key = max(compound.atoms)
            letter = 'a'
        else:
            max_key = max(compound.bonds)
            letter = 'b'
        number = int(max_key[1:])+1
        return "{}{}".format(letter, number)

    def __init__(self, compound, paths={}):
        self._Compound = compound
        self.paths = dict() # { key: set() }
        if paths:
            self.add_paths(**paths)

    def add_paths(self, **paths):
        for reaction, path in paths.iteritems():
            if reaction in self.paths:
                self.paths[reaction].add(path)
            else:
                self.paths[reaction] = set([path])

    def get_paths(self, reaction):
        try:
            return self.paths[reaction]
        except KeyError:
            raise KeyError("{} paths haven't been found yet".format(reaction))

    def _validate_pka(self, pka):
        try:
            self.__dict__['pka']
        except KeyError:
            self.pka = pka
        else:
            if pka != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))

    def __str__(self):
        return "{} of {}".format(self.__class__.__name__, self._Compound.__class__.__name__)

    def __repr__(self):
        return str(self)

    def __getattr__(self, attr):
        return getattr(self._Compound, attr)

    def __eq__(self, other):
        try:
            return self._Compound == other._Compound
        except AttributeError:
            return self._Compound == other

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self._Compound)

    def __getitem__(self, key):
        return self._Compound.__getitem__(key)


class Acid(Reactant):

    def __init__(self, compound, acidic_point, pka, paths={}):
        super(Acid, self).__init__(compound, paths)
        self.acidic_point = acidic_point
        self._validate_pka(pka)


class Base(Reactant):

    def __init__(self, compound, basic_point, pka, paths={}):
        """The pka of a Base should be equal to that of its conjugate
        acid
        """

        super(Base, self).__init__(compound, paths)
        self.conjugate_acid = None
        self.basic_point = basic_point
        self._validate_pka(pka)
        self.to_conjugate_Acid()

    def to_conjugate_Acid(self):
        conjugate = deepcopy(self._Compound)
        a_key = Reactant._new_key(conjugate)
        b_key = Reactant._new_key(conjugate, False)
        hydrogen = compounds.get_Element('H')
        conjugate._add_node_(a_key, hydrogen)
        conjugate._add_edge_(b_key, a_key, self.basic_point)
        self.conjugate_acid = Acid(conjugate, a_key, self.pka, self.paths)


class Product(object):
    _compound = None

    def __init__(self, comp, percentage):
        self._compound = comp
        self.percentage = percentage

    def __getattr__(self, attr):
        return getattr(self._compound, attr)

    def __eq__(self, other):
        try:
            return self._compound == other._compound
        except AttributeError:
            return self._compound == other

    def __str__(self):
        return str(self._compound)

    def __repr__(self):
        return str(self)


class Products(object):

    def __init__(self, maj, min_):
        self._major, self._minor = (), ()
        self.major = maj
        self.minor = min_

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, products):
        if not isinstance(products, types.NoneType):
            for prod in products:
                if isinstance(prod, Product):
                    if isinstance(prod._compound, types.NoneType):
                        continue
                    self._major += (prod,)
                elif isinstance(prod, types.NoneType):
                    continue
                else:
                    raise TypeError(
                            "Should be a Product, not a {}".format(type(prod)))
        else:
            return

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, products):
        if not isinstance(products, types.NoneType):
            for prod in products:
                if isinstance(prod, Product):
                    if isinstance(prod._compound, types.NoneType):
                        continue
                    self._minor += (prod,)
                elif isinstance(prod, types.NoneType):
                    continue
                else:
                    raise TypeError(
                            "Should be a Product, not a {}".format(type(prod)))
        else:
            return

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return not self == other


class EquilibriumProducts(object):
    _reactants = None
    _products = None

    def __init__(self, reactants, products):
        self.reactants = reactants
        self.products = products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, prod):
        self._products = Products(*prod)

    @property
    def reactants(self):
        return self._reactants

    @reactants.setter
    def reactants(self, reactant):
        self._reactants = reactant


class Conditions(object):
    acidic = False
    basic = False
    _neutral = True
    pka = 16
    pka_molecule = None
    pka_location = ''

    def __init__(self, conditions):
        if 'acidic' in conditions and 'basic' in conditions:
            raise ValueError(' '.join(['A molecule is either acidic',
                                         'or basic, not both']))
        if (('acidic' in conditions or 'basic' in conditions) and
                any(item not in conditions
                    for item in ['pka', 'pka_molecule', 'pka_location'])):
            raise ValueError(' '.join(["If conditions aren't neutral the pka",
                                         "must be specified as well as the",
                                         "molecule in question and the",
                                         "specific location (key)"]))
        if 'acidic' in conditions:
            self.acidic = conditions['acidic']
            self.basic = not self.acidic
        elif 'basic' in conditions:
            self.basic = conditions['basic']
            self.acidic = not self.basic
        for k, v in conditions.iteritems():
            if not k in ['acidic', 'basic']:
                setattr(self, k, v)
        self._neutral = not (self.acidic or self.basic)

    @property
    def neutral(self):
        return self._neutral

    def __contains__(self, key):
        return key in self.__dict__

    def __str__(self):
        return "Reaction conditions"

    def __repr__(self):
        return str(self)


class Reaction(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def react(self):
        pass

    @classmethod
    def _remove_node(cls, compound, rem_key):
        compound.atoms.pop(rem_key)
        compound.remove_node(rem_key)

        for k, v in compound.bonds.items():
            if v[0] not in compound.atoms or v[1] not in compound.atoms:
                compound.bonds.pop(k)

        a_ref = cls._rebuild_dict(compound.atoms, 'a')
        new_atoms, new_bonds = {}, {}

        for atom in compound.node:
            new_atoms[a_ref[atom]] = compound.node[atom]['symbol']

        for i, (first, second) in enumerate(compound.edges(), 1):
            endpoints = tuple(sorted((a_ref[first], a_ref[second])))
            rest = ({k:v for k, v in compound.edge[first][second].iteritems()
                     if k != 'key'},)
            new_bonds['b{}'.format(i)] = endpoints + rest

        return new_atoms, new_bonds

    @staticmethod
    def _rebuild_dict(dict_, letter):
        return {key:'{}{}'.format(letter, i)
                 for i, key in enumerate(sorted(dict_), 1)}


if __name__ == '__main__':
    pass
