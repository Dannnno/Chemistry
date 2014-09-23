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

def get_pka(hydrogen):
    
    if len(hydrogen.bonds) == 0: 
        print "H+ is roughly equal to hydronium"
        return
    else: 
        other = hydrogen.bonds[0].get_other(hydrogen)
        if other.name == "Hydrogen": 
            print "H2"
            return 42.
        elif other.name == "Carbon": 
            if (other.is_bonded_to("Carbon") and
                other.is_bonded_to("Oxygen")): pass
            elif other.is_bonded_to("Carbon"): pass
            elif other.is_bonded_to("Oxygen"): pass
            else: raise NotImplementedError
        elif other.name == "Sulfur": 
            if len(other.bonds) == 2:
                print "Thiol"
                return 13.
            else: raise NotImplementedError
        elif other.name == "Nitrogen": 
            if len(other.bonds) == 4:
                print "Positive Nitrogen"
                return 10.
            elif len(other.bonds) == 3:
                print "Amine"
                return 35.
            else: raise NotImplementedError
        elif other.name == "Oxygen": 
            if len(other.bonds) == 2:
                if other.charge > 0:
                    raise NotImplementedError
                elif other.charge < 0:
                    raise NotImplementedError
                else:
                    if other.is_bonded_to("Carbon"):
                        print "Alcohol"
                        return
                    elif other.is_bonded_to("Hydrogen", exclude=[hydrogen]):
                        print "Water"
                        return 15.7
                    else: raise NotImplementedError
            elif len(other.bonds) == 3: 
                if len(filter(lambda x: 
                                x.get_other(other).name == "Hydrogen",
                              other.bonds)) == 3:
                    print "Hydronium"
                    return 
                else: raise NotImplementedError
            else: raise NotImplementedError
        elif other.name in ["Chlorine", "Iodine", "Fluorine", "Bromine"]:
            pass
        else: raise NotImplementedError
    
    raise NotImplementedError