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


import ast
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

get_element_function = """def get_element(symbol):
    \"""Function that returns the appropriate data for a given element.

    Parameters
    ----------
    symbol : string
        The symbol of the atom being returned.

    Returns
    -------
    dict
        A dictionary storing all of the relevant information about an element.
    ""\"

    return periodic_table[symbol]\n\n
"""


def convert_type(cell, typ):
    """Converts a string to a given type, if possible.

    Parameters
    ----------
    cell : string
        The string to be converted
    typ : function
        Function to convert the string

    Returns
    -------
    converted_value
        The new value of the string.

    Notes
    -----
    Credit to SO user Marius for (most of) this function
    http://stackoverflow.com/a/25498445/3076272

    Examples
    --------
    >>> convert_type('4', int)
    4
    >>> convert_type('4.0', float)
    4.0

    If the function can't be applied to that string then it returns
    None
    >>> convert_type('No Data', int) is None
    True
    """

    try:
        return typ(cell)
    except ValueError:
        return None


def build_table():
    """Builds the periodic_table.py file.

    Notes
    -----
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
                         float, float, float, ast.literal_eval, int]
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
