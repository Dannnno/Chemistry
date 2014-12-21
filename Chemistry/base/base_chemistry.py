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

"""Not for public use.  I've been playing around with meta classes and I haven't
decided if they're going to really be necessary as I move forward.  If you're
using this module then you're doing something wrong.
"""

import abc
import sys


class MetaChemistry(type):

    def __new__(cls, clsname, base, dct, *args, **kwargs):
        # print cls, clsname, base, dct, args, kwargs

        return super(MetaChemistry, cls).__new__(cls, clsname, base, dct)


class Chemistry(object):

    __metaclass__ = MetaChemistry

    def __init__(self, input1):
        print(input1)

def reactant_meta_class(clsname, base, dct, *args, **kwargs):
    return MetaChemistry.__new__(MetaChemistry, clsname, base, dct,
                                  *args, **kwargs)

def acid_init(self, atoms, bonds, acidic_point, pka, other_info={}):
    generic_init(self, atoms, bonds, acidic_point, pka, other_info)
    self.acidic_point = self.point

def base_init(self, atoms, bonds, basic_point, pka, other_info={}):
    generic_init(self, atoms, bonds, basic_point, pka, other_info)
    self.basic_point = self.point

def generic_init(self, atoms, bonds, point, pka, other_info):
    self.atoms = atoms
    self.bonds = bonds
    self.other = other_info
    self.point = point
    self._validate_pka(pka)

def _validate_pka(self, pka):
    try:
        self.__dict__['pka']
    except KeyError:
        self.pka = pka
    else:
        if self.pka != pka:
            raise ValueError('pKa must be {}, not {}'.format(self.pka, pka))

def make_Acid(dct):
    return reactant_meta_class("Acid", (Reactant, Chemistry),
                                   {'__module__': __name__,
                                    '__metaclass__': make_Acid,
                                    '__init__': acid_init,
                                    'atoms': {},
                                    'bonds': {},
                                    'pka': None,
                                    'acidic_point': None,
                                    '_validate_pka': _validate_pka})

class Reactant(Chemistry):

    __metaclass__ = reactant_meta_class

    def __init__(self):
        print(self.__dict__)


if __name__ == '__main__':
    #Chemistry(1)
    #Reactant()
    a = make_Acid(None)
    b = a(1, 2, 3, 4, 5)
    print(a)
    print(type(a))
    print(b)
    print(type(b))
