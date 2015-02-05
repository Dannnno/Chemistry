# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository


"""This module is a helper module for building the periodic_table module.  Its
primary purpose is to facilitate the easy rewriting of the periodic table data
if changes need to be made (for example adding or removing data, or updating
data that is found to be incorrect.
"""

__author__ = "Dan Obermiller"


import csv
import json
import os
from collections import OrderedDict


copyright = """# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository\n
"""

mod_doc_string = """
\"""This module stores all of the data about each element in the periodic table.
This includes atomic mass, radius, electronegativity, etc.
\"""
__author__ = "Dan Obermiller"\n\n
"""

get_element_function = """def get_element(symbol='C'):
    \"""Function that returns the appropriate data for a given element.

    Parameters
    ----------
    symbol : string
        The symbol of the atom being returned.  Defaults to 'C' for Carbon.

    Returns
    -------
    table : dict
        A dictionary storing all of the relevant information about an element.
    ""\"

    table = {"symbol": symbol}
    table.update(periodic_table[symbol])
    return table\n\n
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
    None
    >>> convert_type('No Data', int) is None
    True
    """

    try:
        if typ is str_to_list:
            return typ(cell, mapped=int)
        return typ(cell)
    except ValueError:
        return None


def str_to_list(a_stringy_list, mapped=None):
    """Takes a string that looks like a list and makes it a list

    >>> str_to_list("[1,2,3]")
    ['1', '2', '3']

    If a function to be mapped is provided it will attempt to do so
    >>> str_to_list("[1,2,3]", mapped=int)
    [1, 2, 3]
    """

    the_list = a_stringy_list[1:-1].split(",")
    return map(mapped, the_list)


def build_table():
    """Builds the periodic_table.py file if it hasn't been created yet.

    The function exists to ease large scale changes to the data held within the
    periodic table
    """
    curdir = os.getcwd()
    local_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(local_dir)
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

        periodic_table.write(copyright)
        periodic_table.write(mod_doc_string)
        periodic_table.write(get_element_function)
        json_table = json.dumps(per_table, indent=4).split('\n')
        json_table[0] = "periodic_table = " + json_table[0]

        for i in range(1, len(json_table)):
            json_table[i] = "               " + json_table[i]

        for line in json_table:
            periodic_table.write(line.replace('null', 'None') + "\n")
    os.chdir(curdir)
