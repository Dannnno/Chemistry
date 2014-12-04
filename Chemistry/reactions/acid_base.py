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
    
    def __init__(self, acid, base, conditions):
        ## Validating the conditions
        if not isinstance(conditions, Conditions):
            raise TypeError("{} must be Conditions, is {}"
                                .format(conditions, type(conditions)))
                                
        self.conditions = conditions
        if not self.conditions['neutral']:
            if self.conditions['acidic']:
                results = Reactant._compare_pkas(acid, base, self.conditions)
                if isinstance(results[0], Conditions): pass
                elif isinstance(results[1], Conditions): pass
                else: pass
            elif self.conditions['basic']:
                results = Reactant._compare_pkas(acid, base, self.conditions)
                if isinstance(results[0], Conditions): pass
                elif isinstance(results[1], Conditions): pass
                else: pass
            else:
                raise ValueError("Non-neutral conditions must be basic or acidic")
        else:
            acid, base = Reactant._compare_pkas(acid, base)
            
        conditions_location = 1
 
 
        ## Validating the acid and base)
        if not isinstance(acid, Acid):
            raise TypeError("{} must be an Acid, is a {}"
                                .format(acid, type(acid)))
        if not isinstance(base, Base):
            raise TypeError("{} must be an Base, is a {}"
                                .format(base, type(base)))
        self.acid = acid
        self.base = base
        
        
    def react(self):
        raise NotImplementedError
