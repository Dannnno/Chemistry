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

from Chemistry import compounds, base_reactions
from Chemistry.base_reactions import Acid, Base, Reactant, \
                                         Reaction, Conditions, Product


class AcidBase(Reaction):
    _conditions = None
    _acid, _base = (), ()
    _acidic_point, _basic_point = (), ()

    def __init__(self, acid, base, cond):
        self.conditions = cond
        self.acid = acid
        self.base = base

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, cond):
        if isinstance(cond, dict):
            self.conditions = Conditions(cond)
        elif isinstance(cond, Conditions):
            self._conditions = cond
        else:
            raise TypeError("Conditions must be a Conditions object")

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, acid_):
        if self.conditions.acidic:
            if self.conditions.pka < acid_.pka:
                self._acid = (self.conditions.pka_molecule, False)
            else:
                self._acid = (acid_, True)
        else:
            self._acid = (acid_, True)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base_):
        if self.conditions.basic:
            if self.conditions.pka > base_.pka:
                self._base = (self.conditions.pka_molecule, False)
            else:
                self._base = (base_, True)
        else:
            self._base = (base_, True)

    @property
    def acidic_point(self):
        return self._acidic_point

    @property
    def basic_point(self):
        return self._basic_point

    def react(self):
        raise NotImplementedError
