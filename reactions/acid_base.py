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

import compounds
import base_reactions
from base_reactions import Acid, Base, Reaction, Conditions


class AcidBase(Reaction):
    
    def __init__(self, acid, base, conditions):
        ## Validating the acid and base)
        if not isinstance(acid, Acid):
            raise TypeError("{} must be an Acid, is a {}"
                                .format(acid, type(acid)))
        if not isinstance(base, Base):
            raise TypeError("{} must be an Base, is a {}"
                                .format(base, type(base)))
        self.acid = acid
        self.base = base
        
        ## Validating the conditions
        if not isinstance(conditions, Conditions):
            raise TypeError("{} must be Conditions, is {}"
                                .format(conditions, type(conditions)))
        if not conditions.has_reactants():
            conditions.add_reactants(acid, base) 
        elif not conditions.validate_reactants(acid, base):
            raise ValueError(
                '\t'.join(["Condition must have the correct reactants",
                           "has {} instead of",
                           "{}"]).format(conditions.reactants, [acid, base]))
        
        self.conditions = conditions                    
        