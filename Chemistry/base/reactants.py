# Copyright (c) 2014 Dan Obermiller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# You should have received a copy of the MIT License along with this program.
# If not, see <http://opensource.org/licenses/MIT>

from copy import deepcopy

import Chemistry.base.periodic_table as pt
from Chemistry.base.compounds import _CompoundWrapper


class Reactant(_CompoundWrapper):
    """The base Reactant object.  All subclasses of this are things that
    are commonly found in a reaction
    """

    @classmethod
    def make_Base(cls, basic_compound, pka, point):
        """Classmethod that turns a compound into a base."""

        if isinstance(basic_compound, Base):
            return basic_compound
        else:
            return Base(basic_compound, point, pka)

    @classmethod
    def make_Acid(cls, acidic_compound, pka, point):
        """Basically the same as make_Base, but it makes acids"""

        if isinstance(acidic_compound, Acid):
            return acidic_compound
        else:
            return Acid(acidic_compound, point, pka)

    @classmethod
    def _new_key(cls, compound, atom=True):
        """Generates a new atom/bond key for a compound"""

        if atom:
            max_key = max(compound.atoms)
            letter = 'a'
        else:
            max_key = max(compound.bonds)
            letter = 'b'
        number = int(max_key[1:])+1
        return "{}{}".format(letter, number)

    def __init__(self, compound):
        super(Reactant, self).__init__(compound)

    def _validate_pka(self, pka):
        """Validates the pKa of a molecule.  This should move into a property"""

        try:
            _ = self.__dict__['pka']
        except KeyError:
            self.pka = pka
        else:
            if pka != self.pka:
                raise ValueError("pKa must equal {}".format(self.pka))

    def __str__(self):
        return "{} of {}".format(self.__class__.__name__,
                                 self.compound.__class__.__name__)

    def __repr__(self):
        return str(self)


class Acid(Reactant):
    """A subclass of Reactant, represents acidic compounds in a reaction"""

    def __init__(self, compound, acidic_point, pka):
        super(Acid, self).__init__(compound)
        self.acidic_point = acidic_point
        self._validate_pka(pka)

    def to_conjugate_base(self, *args, **kwargs):
        """Transforms the current acid into its conjugate base"""

        raise NotImplementedError


class Base(Reactant):
    """A subclass of Reactant, represents basic compounds in a reaction"""

    def __init__(self, compound, basic_point, pka):
        """The pka of a Base should be equal to that of its conjugate acid."""

        super(Base, self).__init__(compound)
        self.basic_point = basic_point
        self._validate_pka(pka)

    def to_conjugate_acid(self):
        """Transforms the current base into its conjugate acid"""

        conjugate = deepcopy(self.compound)
        a_key = Reactant._new_key(conjugate)
        b_key = Reactant._new_key(conjugate, False)
        hydrogen = pt.get_element('H')
        conjugate._add_node(a_key, hydrogen)
        conjugate._add_edge(b_key, a_key, self.basic_point)
        try:
            conjugate.other_info['id'] = \
                "Conjugate acid of {}".format(self.other_info['id'])
        except KeyError:
            conjugate.other_info['id'] = "Unknown acid"
        return Acid(conjugate, a_key, self.pka)


class LewisAcid(Acid): pass


class LewisBase(Base): pass


class BronstedAcid(Acid): pass


class BronstedBase(Base): pass


class Electrophile(Reactant): pass


class Nucleophile(Reactant): pass
