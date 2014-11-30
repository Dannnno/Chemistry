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

import csv
import json
from collections import OrderedDict


copyright = """\"\"\"
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
\"\"\"

ENEG = "Electronegativity"
GROUP = "Group"
MP = "Melting Point"
WEIGHT = "Weight"
DENSITY = "Density"
SYMB = "Symbol"
ELEMENT = "Element"
NUMBER = "Atomic Number"
BP = "Boiling Point"
HEAT = "Heat of ?"
RAD = "Atomic Radius"
OX = "Oxidation Number(s)"
"""  

def convert_type(cell, typ):
    """Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Takes a string and a function that the string should be represented as,
    if possible.  
    
    >>> convert_type('4', int)
    4
    >>> convert_type('4.0', float)
    4.0
    >>> convert_type('[1,2,3]', str_to_list)
    [1, 2, 3]
    
    If the function can't be applied to that string then it returns
    "No_Data"
    >>> convert_type('No Data', int)
    'No_Data'
    """

    try:
        if typ is str_to_list:
            return typ(cell, mapped=int)
        return typ(cell)
    except (TypeError, ValueError):
        return "No_Data" # The nomiker I have chosen for missing data
        
def str_to_list(a_stringy_list, mapped=None):
    """Takes a string that looks like a list and makes it a list
    
    >>> str_to_list("[1,2,3]")
    ['1', '2', '3']
    
    If a function to be mapped is provided it will attempt to do so
    >>> str_to_list("[1,2,3]", mapped=int)
    [1, 2, 3]
    """
    
    the_list = a_stringy_list[1:-1].split(",")
    try:
        # Fun fact, mapping 'None' to a list just returns the list
        return map(mapped, the_list)
    except ValueError: #Exception:
        ## print "Function %s couldn't be mapped to list " % str(mapped), the_list
        return the_list
      
def build_table():  
    with open("element_list.csv", 'r') as element_data, \
        open("periodic_table.py", 'w') as periodic_table:
            
        per_table = OrderedDict()
        element_reader = csv.reader(element_data)
        header = element_reader.next()
        for i in range(118):
            tl = element_reader.next()
            col_types = [int, str, str, int, float, float, float,
                        float, float, float, float, str_to_list]
            new_row = dict(zip(header, tuple(convert_type(cell, typ)
                            for cell, typ in zip(tl, col_types))))
            per_table[tl[1]] = new_row
        
        periodic_table.write(copyright + '\n\n')
        json_table = json.dumps(per_table, indent=4).split('\n')
        json_table[0] = "periodic_table = " + json_table[0]
        
        for i in range(1, len(json_table)):
            json_table[i] = "               " + json_table[i]
        
        for line in json_table:
            periodic_table.write(line + "\n")
        
if __name__ == "__main__":
    import os
    #print os.getcwd()
    #os.chdir(os.getcwd() + "/desktop/programming/github/chemistry")
    build_table()