# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository


"""This module stores all of the data about each element in the periodic table.
This includes atomic mass, radius, electronegativity, etc.
"""
__author__ = "Dan Obermiller"


def get_element(symbol):
    """Function that returns the appropriate data for a given element.

    Parameters
    ----------
    symbol : string
        The symbol of the atom being returned.

    Returns
    -------
    dict
        A dictionary storing all of the relevant information about an element.
    """

    return periodic_table[symbol]


periodic_table = {
                   "H": {
                       "Electronegativity": 2.2, 
                       "Group": 1, 
                       "Melting Point": 14.01, 
                       "Weight": 1.008, 
                       "Density": 8.988e-05, 
                       "Symbol": "H", 
                       "Element": "Hydrogen", 
                       "Atomic Number": 1, 
                       "Boiling Point": 20.28, 
                       "Atomic Radius": 53.0, 
                       "Oxidation Number(s)": [
                           1, 
                           -1
                       ]
                   }, 
                   "He": {
                       "Electronegativity": None, 
                       "Group": 18, 
                       "Melting Point": 0.956, 
                       "Weight": 4.002602, 
                       "Density": 0.0001785, 
                       "Symbol": "He", 
                       "Element": "Helium", 
                       "Atomic Number": 2, 
                       "Boiling Point": 4.22, 
                       "Atomic Radius": 31.0, 
                       "Oxidation Number(s)": [
                           0
                       ]
                   }, 
                   "Li": {
                       "Electronegativity": 0.98, 
                       "Group": 1, 
                       "Melting Point": 453.69, 
                       "Weight": 6.94, 
                       "Density": 0.534, 
                       "Symbol": "Li", 
                       "Element": "Lithium", 
                       "Atomic Number": 3, 
                       "Boiling Point": 1560.0, 
                       "Atomic Radius": 167.0, 
                       "Oxidation Number(s)": [
                           1
                       ]
                   }, 
                   "Be": {
                       "Electronegativity": 1.57, 
                       "Group": 2, 
                       "Melting Point": 1560.0, 
                       "Weight": 9.012182, 
                       "Density": 1.85, 
                       "Symbol": "Be", 
                       "Element": "Beryllium", 
                       "Atomic Number": 4, 
                       "Boiling Point": 2742.0, 
                       "Atomic Radius": 112.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "B": {
                       "Electronegativity": 2.04, 
                       "Group": 13, 
                       "Melting Point": 2349.0, 
                       "Weight": 10.81, 
                       "Density": 2.34, 
                       "Symbol": "B", 
                       "Element": "Boron", 
                       "Atomic Number": 5, 
                       "Boiling Point": 4200.0, 
                       "Atomic Radius": 87.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "C": {
                       "Electronegativity": 2.55, 
                       "Group": 14, 
                       "Melting Point": 3800.0, 
                       "Weight": 12.011, 
                       "Density": 2.267, 
                       "Symbol": "C", 
                       "Element": "Carbon", 
                       "Atomic Number": 6, 
                       "Boiling Point": 4300.0, 
                       "Atomic Radius": 67.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           -4, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "N": {
                       "Electronegativity": 3.04, 
                       "Group": 15, 
                       "Melting Point": 63.15, 
                       "Weight": 14.007, 
                       "Density": 0.0012506, 
                       "Symbol": "N", 
                       "Element": "Nitrogen", 
                       "Atomic Number": 7, 
                       "Boiling Point": 77.36, 
                       "Atomic Radius": 56.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "O": {
                       "Electronegativity": 3.44, 
                       "Group": 16, 
                       "Melting Point": 54.36, 
                       "Weight": 15.999, 
                       "Density": 0.001429, 
                       "Symbol": "O", 
                       "Element": "Oxygen", 
                       "Atomic Number": 8, 
                       "Boiling Point": 90.2, 
                       "Atomic Radius": 48.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           -2, 
                           -1
                       ]
                   }, 
                   "F": {
                       "Electronegativity": 3.98, 
                       "Group": 17, 
                       "Melting Point": 53.53, 
                       "Weight": 18.9984032, 
                       "Density": 0.001696, 
                       "Symbol": "F", 
                       "Element": "Fluorine", 
                       "Atomic Number": 9, 
                       "Boiling Point": 85.03, 
                       "Atomic Radius": 42.0, 
                       "Oxidation Number(s)": [
                           -1
                       ]
                   }, 
                   "Ne": {
                       "Electronegativity": None, 
                       "Group": 18, 
                       "Melting Point": 24.56, 
                       "Weight": 20.1797, 
                       "Density": 0.0008999, 
                       "Symbol": "Ne", 
                       "Element": "Neon", 
                       "Atomic Number": 10, 
                       "Boiling Point": 27.07, 
                       "Atomic Radius": 38.0, 
                       "Oxidation Number(s)": [
                           0
                       ]
                   }, 
                   "Na": {
                       "Electronegativity": 0.93, 
                       "Group": 1, 
                       "Melting Point": 370.87, 
                       "Weight": 22.98976928, 
                       "Density": 0.971, 
                       "Symbol": "Na", 
                       "Element": "Sodium", 
                       "Atomic Number": 11, 
                       "Boiling Point": 1156.0, 
                       "Atomic Radius": 190.0, 
                       "Oxidation Number(s)": [
                           1, 
                           -1
                       ]
                   }, 
                   "Mg": {
                       "Electronegativity": 1.31, 
                       "Group": 2, 
                       "Melting Point": 923.0, 
                       "Weight": 24.3059, 
                       "Density": 1.738, 
                       "Symbol": "Mg", 
                       "Element": "Magnesium", 
                       "Atomic Number": 12, 
                       "Boiling Point": 1363.0, 
                       "Atomic Radius": 145.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "Al": {
                       "Electronegativity": 1.61, 
                       "Group": 13, 
                       "Melting Point": 933.47, 
                       "Weight": 26.9815386, 
                       "Density": 2.698, 
                       "Symbol": "Al", 
                       "Element": "Aluminium", 
                       "Atomic Number": 13, 
                       "Boiling Point": 2792.0, 
                       "Atomic Radius": 118.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Si": {
                       "Electronegativity": 1.9, 
                       "Group": 14, 
                       "Melting Point": 1687.0, 
                       "Weight": 28.085, 
                       "Density": 2.3296, 
                       "Symbol": "Si", 
                       "Element": "Silicon", 
                       "Atomic Number": 14, 
                       "Boiling Point": 3538.0, 
                       "Atomic Radius": 111.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           -4, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "P": {
                       "Electronegativity": 2.19, 
                       "Group": 15, 
                       "Melting Point": 317.3, 
                       "Weight": 30.973762, 
                       "Density": 1.82, 
                       "Symbol": "P", 
                       "Element": "Phosphorus", 
                       "Atomic Number": 15, 
                       "Boiling Point": 550.0, 
                       "Atomic Radius": 98.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "S": {
                       "Electronegativity": 2.58, 
                       "Group": 16, 
                       "Melting Point": 388.36, 
                       "Weight": 32.06, 
                       "Density": 2.067, 
                       "Symbol": "S", 
                       "Element": "Sulfur", 
                       "Atomic Number": 16, 
                       "Boiling Point": 717.87, 
                       "Atomic Radius": 88.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -1
                       ]
                   }, 
                   "Cl": {
                       "Electronegativity": 3.16, 
                       "Group": 17, 
                       "Melting Point": 171.6, 
                       "Weight": 35.45, 
                       "Density": 0.003214, 
                       "Symbol": "Cl", 
                       "Element": "Chlorine", 
                       "Atomic Number": 17, 
                       "Boiling Point": 239.11, 
                       "Atomic Radius": 79.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           -1
                       ]
                   }, 
                   "Ar": {
                       "Electronegativity": None, 
                       "Group": 18, 
                       "Melting Point": 83.8, 
                       "Weight": 39.948, 
                       "Density": 0.0017837, 
                       "Symbol": "Ar", 
                       "Element": "Argon", 
                       "Atomic Number": 18, 
                       "Boiling Point": 87.3, 
                       "Atomic Radius": 71.0, 
                       "Oxidation Number(s)": [
                           0
                       ]
                   }, 
                   "K": {
                       "Electronegativity": 0.82, 
                       "Group": 1, 
                       "Melting Point": 336.53, 
                       "Weight": 39.0983, 
                       "Density": 0.862, 
                       "Symbol": "K", 
                       "Element": "Potassium", 
                       "Atomic Number": 19, 
                       "Boiling Point": 1032.0, 
                       "Atomic Radius": 243.0, 
                       "Oxidation Number(s)": [
                           1, 
                           -1
                       ]
                   }, 
                   "Ca": {
                       "Electronegativity": 1.0, 
                       "Group": 2, 
                       "Melting Point": 1115.0, 
                       "Weight": 40.078, 
                       "Density": 1.54, 
                       "Symbol": "Ca", 
                       "Element": "Calcium", 
                       "Atomic Number": 20, 
                       "Boiling Point": 1757.0, 
                       "Atomic Radius": 194.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "Sc": {
                       "Electronegativity": 1.36, 
                       "Group": 3, 
                       "Melting Point": 1814.0, 
                       "Weight": 44.955912, 
                       "Density": 2.989, 
                       "Symbol": "Sc", 
                       "Element": "Scandium", 
                       "Atomic Number": 21, 
                       "Boiling Point": 3109.0, 
                       "Atomic Radius": 184.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Ti": {
                       "Electronegativity": 1.54, 
                       "Group": 4, 
                       "Melting Point": 1941.0, 
                       "Weight": 47.867, 
                       "Density": 4.54, 
                       "Symbol": "Ti", 
                       "Element": "Titanium", 
                       "Atomic Number": 22, 
                       "Boiling Point": 3560.0, 
                       "Atomic Radius": 176.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           -1
                       ]
                   }, 
                   "V": {
                       "Electronegativity": 1.63, 
                       "Group": 5, 
                       "Melting Point": 2183.0, 
                       "Weight": 50.9415, 
                       "Density": 6.11, 
                       "Symbol": "V", 
                       "Element": "Vanadium", 
                       "Atomic Number": 23, 
                       "Boiling Point": 3680.0, 
                       "Atomic Radius": 171.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           -1
                       ]
                   }, 
                   "Cr": {
                       "Electronegativity": 1.66, 
                       "Group": 6, 
                       "Melting Point": 2180.0, 
                       "Weight": 51.9961, 
                       "Density": 7.15, 
                       "Symbol": "Cr", 
                       "Element": "Chromium", 
                       "Atomic Number": 24, 
                       "Boiling Point": 2944.0, 
                       "Atomic Radius": 166.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Mn": {
                       "Electronegativity": 1.55, 
                       "Group": 7, 
                       "Melting Point": 1519.0, 
                       "Weight": 54.938045, 
                       "Density": 7.44, 
                       "Symbol": "Mn", 
                       "Element": "Manganese", 
                       "Atomic Number": 25, 
                       "Boiling Point": 2334.0, 
                       "Atomic Radius": 161.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Fe": {
                       "Electronegativity": 1.83, 
                       "Group": 8, 
                       "Melting Point": 1811.0, 
                       "Weight": 55.845, 
                       "Density": 7.874, 
                       "Symbol": "Fe", 
                       "Element": "Iron", 
                       "Atomic Number": 26, 
                       "Boiling Point": 3134.0, 
                       "Atomic Radius": 156.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Co": {
                       "Electronegativity": 1.88, 
                       "Group": 9, 
                       "Melting Point": 1768.0, 
                       "Weight": 58.933195, 
                       "Density": 8.86, 
                       "Symbol": "Co", 
                       "Element": "Cobalt", 
                       "Atomic Number": 27, 
                       "Boiling Point": 3200.0, 
                       "Atomic Radius": 152.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           -1
                       ]
                   }, 
                   "Ni": {
                       "Electronegativity": 1.91, 
                       "Group": 10, 
                       "Melting Point": 1728.0, 
                       "Weight": 58.6934, 
                       "Density": 8.912, 
                       "Symbol": "Ni", 
                       "Element": "Nickel", 
                       "Atomic Number": 28, 
                       "Boiling Point": 3186.0, 
                       "Atomic Radius": 149.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           -1
                       ]
                   }, 
                   "Cu": {
                       "Electronegativity": 1.9, 
                       "Group": 11, 
                       "Melting Point": 1357.77, 
                       "Weight": 63.546, 
                       "Density": 8.96, 
                       "Symbol": "Cu", 
                       "Element": "Copper", 
                       "Atomic Number": 29, 
                       "Boiling Point": 2835.0, 
                       "Atomic Radius": 145.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Zn": {
                       "Electronegativity": 1.65, 
                       "Group": 12, 
                       "Melting Point": 692.88, 
                       "Weight": 65.38, 
                       "Density": 7.134, 
                       "Symbol": "Zn", 
                       "Element": "Zinc", 
                       "Atomic Number": 30, 
                       "Boiling Point": 1180.0, 
                       "Atomic Radius": 142.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "Ga": {
                       "Electronegativity": 1.81, 
                       "Group": 13, 
                       "Melting Point": 302.9146, 
                       "Weight": 69.723, 
                       "Density": 5.907, 
                       "Symbol": "Ga", 
                       "Element": "Gallium", 
                       "Atomic Number": 31, 
                       "Boiling Point": 2477.0, 
                       "Atomic Radius": 136.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Ge": {
                       "Electronegativity": 2.01, 
                       "Group": 14, 
                       "Melting Point": 1211.4, 
                       "Weight": 72.63, 
                       "Density": 5.323, 
                       "Symbol": "Ge", 
                       "Element": "Germanium", 
                       "Atomic Number": 32, 
                       "Boiling Point": 3106.0, 
                       "Atomic Radius": 125.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           -4, 
                           -3, 
                           -2, 
                           -1
                       ]
                   }, 
                   "As": {
                       "Electronegativity": 2.18, 
                       "Group": 15, 
                       "Melting Point": 1090.0, 
                       "Weight": 74.9216, 
                       "Density": 5.776, 
                       "Symbol": "As", 
                       "Element": "Arsenic", 
                       "Atomic Number": 33, 
                       "Boiling Point": 887.0, 
                       "Atomic Radius": 114.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           5, 
                           -3
                       ]
                   }, 
                   "Se": {
                       "Electronegativity": 2.55, 
                       "Group": 16, 
                       "Melting Point": 453.0, 
                       "Weight": 78.96, 
                       "Density": 4.809, 
                       "Symbol": "Se", 
                       "Element": "Selenium", 
                       "Atomic Number": 34, 
                       "Boiling Point": 958.0, 
                       "Atomic Radius": 103.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           4, 
                           6, 
                           -2
                       ]
                   }, 
                   "Br": {
                       "Electronegativity": 2.96, 
                       "Group": 17, 
                       "Melting Point": 265.8, 
                       "Weight": 79.9049, 
                       "Density": 3.122, 
                       "Symbol": "Br", 
                       "Element": "Bromine", 
                       "Atomic Number": 35, 
                       "Boiling Point": 332.0, 
                       "Atomic Radius": 94.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           7, 
                           -1
                       ]
                   }, 
                   "Kr": {
                       "Electronegativity": 3.0, 
                       "Group": 18, 
                       "Melting Point": 115.79, 
                       "Weight": 83.798, 
                       "Density": 0.003733, 
                       "Symbol": "Kr", 
                       "Element": "Krypton", 
                       "Atomic Number": 36, 
                       "Boiling Point": 119.93, 
                       "Atomic Radius": 88.0, 
                       "Oxidation Number(s)": [
                           2
                       ]
                   }, 
                   "Rb": {
                       "Electronegativity": 0.82, 
                       "Group": 1, 
                       "Melting Point": 312.46, 
                       "Weight": 85.4678, 
                       "Density": 1.532, 
                       "Symbol": "Rb", 
                       "Element": "Rubidium", 
                       "Atomic Number": 37, 
                       "Boiling Point": 961.0, 
                       "Atomic Radius": 265.0, 
                       "Oxidation Number(s)": [
                           1, 
                           -1
                       ]
                   }, 
                   "Sr": {
                       "Electronegativity": 0.95, 
                       "Group": 2, 
                       "Melting Point": 1050.0, 
                       "Weight": 87.62, 
                       "Density": 2.64, 
                       "Symbol": "Sr", 
                       "Element": "Strontium", 
                       "Atomic Number": 38, 
                       "Boiling Point": 1655.0, 
                       "Atomic Radius": 219.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "Y": {
                       "Electronegativity": 1.22, 
                       "Group": 3, 
                       "Melting Point": 1799.0, 
                       "Weight": 88.90585, 
                       "Density": 4.469, 
                       "Symbol": "Y", 
                       "Element": "Yttrium", 
                       "Atomic Number": 39, 
                       "Boiling Point": 3609.0, 
                       "Atomic Radius": 212.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Zr": {
                       "Electronegativity": 1.33, 
                       "Group": 4, 
                       "Melting Point": 2128.0, 
                       "Weight": 91.224, 
                       "Density": 6.506, 
                       "Symbol": "Zr", 
                       "Element": "Zirconium", 
                       "Atomic Number": 40, 
                       "Boiling Point": 4682.0, 
                       "Atomic Radius": 206.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Nb": {
                       "Electronegativity": 1.6, 
                       "Group": 5, 
                       "Melting Point": 2750.0, 
                       "Weight": 92.90638, 
                       "Density": 8.57, 
                       "Symbol": "Nb", 
                       "Element": "Niobium", 
                       "Atomic Number": 41, 
                       "Boiling Point": 5017.0, 
                       "Atomic Radius": 198.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           -1
                       ]
                   }, 
                   "Mo": {
                       "Electronegativity": 2.16, 
                       "Group": 6, 
                       "Melting Point": 2896.0, 
                       "Weight": 95.96, 
                       "Density": 10.22, 
                       "Symbol": "Mo", 
                       "Element": "Molybdenum", 
                       "Atomic Number": 42, 
                       "Boiling Point": 4912.0, 
                       "Atomic Radius": 190.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Tc": {
                       "Electronegativity": 1.9, 
                       "Group": 7, 
                       "Melting Point": 2430.0, 
                       "Weight": 98.0, 
                       "Density": 11.5, 
                       "Symbol": "Tc", 
                       "Element": "Technetium", 
                       "Atomic Number": 43, 
                       "Boiling Point": 4538.0, 
                       "Atomic Radius": 183.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           -3, 
                           -1
                       ]
                   }, 
                   "Ru": {
                       "Electronegativity": 2.2, 
                       "Group": 8, 
                       "Melting Point": 2607.0, 
                       "Weight": 101.07, 
                       "Density": 12.37, 
                       "Symbol": "Ru", 
                       "Element": "Ruthenium", 
                       "Atomic Number": 44, 
                       "Boiling Point": 4423.0, 
                       "Atomic Radius": 178.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           8, 
                           -2
                       ]
                   }, 
                   "Rh": {
                       "Electronegativity": 2.28, 
                       "Group": 9, 
                       "Melting Point": 2237.0, 
                       "Weight": 102.9055, 
                       "Density": 12.41, 
                       "Symbol": "Rh", 
                       "Element": "Rhodium", 
                       "Atomic Number": 45, 
                       "Boiling Point": 3968.0, 
                       "Atomic Radius": 173.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -1
                       ]
                   }, 
                   "Pd": {
                       "Electronegativity": 2.2, 
                       "Group": 10, 
                       "Melting Point": 1828.05, 
                       "Weight": 106.42, 
                       "Density": 12.02, 
                       "Symbol": "Pd", 
                       "Element": "Palladium", 
                       "Atomic Number": 46, 
                       "Boiling Point": 3236.0, 
                       "Atomic Radius": 169.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           4, 
                           6
                       ]
                   }, 
                   "Ag": {
                       "Electronegativity": 1.93, 
                       "Group": 11, 
                       "Melting Point": 1234.93, 
                       "Weight": 107.8682, 
                       "Density": 10.501, 
                       "Symbol": "Ag", 
                       "Element": "Silver", 
                       "Atomic Number": 47, 
                       "Boiling Point": 2435.0, 
                       "Atomic Radius": 165.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Cd": {
                       "Electronegativity": 1.69, 
                       "Group": 12, 
                       "Melting Point": 594.22, 
                       "Weight": 112.411, 
                       "Density": 8.69, 
                       "Symbol": "Cd", 
                       "Element": "Cadmium", 
                       "Atomic Number": 48, 
                       "Boiling Point": 1040.0, 
                       "Atomic Radius": 161.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2
                       ]
                   }, 
                   "In": {
                       "Electronegativity": 1.78, 
                       "Group": 13, 
                       "Melting Point": 429.75, 
                       "Weight": 114.818, 
                       "Density": 7.31, 
                       "Symbol": "In", 
                       "Element": "Indium", 
                       "Atomic Number": 49, 
                       "Boiling Point": 2345.0, 
                       "Atomic Radius": 156.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Sn": {
                       "Electronegativity": 1.96, 
                       "Group": 14, 
                       "Melting Point": 505.08, 
                       "Weight": 118.71, 
                       "Density": 7.287, 
                       "Symbol": "Sn", 
                       "Element": "Tin", 
                       "Atomic Number": 50, 
                       "Boiling Point": 2875.0, 
                       "Atomic Radius": 145.0, 
                       "Oxidation Number(s)": [
                           2, 
                           4, 
                           -4
                       ]
                   }, 
                   "Sb": {
                       "Electronegativity": 2.05, 
                       "Group": 15, 
                       "Melting Point": 903.78, 
                       "Weight": 121.76, 
                       "Density": 6.685, 
                       "Symbol": "Sb", 
                       "Element": "Antimony", 
                       "Atomic Number": 51, 
                       "Boiling Point": 1860.0, 
                       "Atomic Radius": 133.0, 
                       "Oxidation Number(s)": [
                           3, 
                           5, 
                           -3
                       ]
                   }, 
                   "Te": {
                       "Electronegativity": 2.1, 
                       "Group": 16, 
                       "Melting Point": 722.66, 
                       "Weight": 127.6, 
                       "Density": 6.232, 
                       "Symbol": "Te", 
                       "Element": "Tellurium", 
                       "Atomic Number": 52, 
                       "Boiling Point": 1261.0, 
                       "Atomic Radius": 123.0, 
                       "Oxidation Number(s)": [
                           2, 
                           4, 
                           5, 
                           6, 
                           -2
                       ]
                   }, 
                   "I": {
                       "Electronegativity": 2.66, 
                       "Group": 17, 
                       "Melting Point": 386.85, 
                       "Weight": 126.90447, 
                       "Density": 4.93, 
                       "Symbol": "I", 
                       "Element": "Iodine", 
                       "Atomic Number": 53, 
                       "Boiling Point": 457.4, 
                       "Atomic Radius": 115.0, 
                       "Oxidation Number(s)": [
                           1, 
                           3, 
                           4, 
                           5, 
                           7, 
                           -1
                       ]
                   }, 
                   "Xe": {
                       "Electronegativity": 2.6, 
                       "Group": 18, 
                       "Melting Point": 161.4, 
                       "Weight": 131.293, 
                       "Density": 0.005887, 
                       "Symbol": "Xe", 
                       "Element": "Xenon", 
                       "Atomic Number": 54, 
                       "Boiling Point": 165.03, 
                       "Atomic Radius": 108.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           4, 
                           6, 
                           8
                       ]
                   }, 
                   "Cs": {
                       "Electronegativity": 0.79, 
                       "Group": 1, 
                       "Melting Point": 301.59, 
                       "Weight": 132.9054519, 
                       "Density": 1.873, 
                       "Symbol": "Cs", 
                       "Element": "Caesium", 
                       "Atomic Number": 55, 
                       "Boiling Point": 944.0, 
                       "Atomic Radius": 298.0, 
                       "Oxidation Number(s)": [
                           1, 
                           -1
                       ]
                   }, 
                   "Ba": {
                       "Electronegativity": 0.89, 
                       "Group": 2, 
                       "Melting Point": 1000.0, 
                       "Weight": 137.327, 
                       "Density": 3.594, 
                       "Symbol": "Ba", 
                       "Element": "Barium", 
                       "Atomic Number": 56, 
                       "Boiling Point": 2170.0, 
                       "Atomic Radius": 253.0, 
                       "Oxidation Number(s)": [
                           2
                       ]
                   }, 
                   "La": {
                       "Electronegativity": 1.1, 
                       "Group": 0, 
                       "Melting Point": 1193.0, 
                       "Weight": 138.90547, 
                       "Density": 6.145, 
                       "Symbol": "La", 
                       "Element": "Lanthanum", 
                       "Atomic Number": 57, 
                       "Boiling Point": 3737.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Ce": {
                       "Electronegativity": 1.12, 
                       "Group": 0, 
                       "Melting Point": 1068.0, 
                       "Weight": 140.116, 
                       "Density": 6.77, 
                       "Symbol": "Ce", 
                       "Element": "Cerium", 
                       "Atomic Number": 58, 
                       "Boiling Point": 3716.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Pr": {
                       "Electronegativity": 1.13, 
                       "Group": 0, 
                       "Melting Point": 1208.0, 
                       "Weight": 140.90765, 
                       "Density": 6.773, 
                       "Symbol": "Pr", 
                       "Element": "Praseodymium", 
                       "Atomic Number": 59, 
                       "Boiling Point": 3793.0, 
                       "Atomic Radius": 247.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Nd": {
                       "Electronegativity": 1.14, 
                       "Group": 0, 
                       "Melting Point": 1297.0, 
                       "Weight": 144.242, 
                       "Density": 7.007, 
                       "Symbol": "Nd", 
                       "Element": "Neodymium", 
                       "Atomic Number": 60, 
                       "Boiling Point": 3347.0, 
                       "Atomic Radius": 206.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Pm": {
                       "Electronegativity": 1.13, 
                       "Group": 0, 
                       "Melting Point": 1315.0, 
                       "Weight": 145.0, 
                       "Density": 7.26, 
                       "Symbol": "Pm", 
                       "Element": "Promethium", 
                       "Atomic Number": 61, 
                       "Boiling Point": 3273.0, 
                       "Atomic Radius": 205.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Sm": {
                       "Electronegativity": 1.17, 
                       "Group": 0, 
                       "Melting Point": 1345.0, 
                       "Weight": 150.36, 
                       "Density": 7.52, 
                       "Symbol": "Sm", 
                       "Element": "Samarium", 
                       "Atomic Number": 62, 
                       "Boiling Point": 2067.0, 
                       "Atomic Radius": 238.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Eu": {
                       "Electronegativity": 1.2, 
                       "Group": 0, 
                       "Melting Point": 1099.0, 
                       "Weight": 151.964, 
                       "Density": 5.243, 
                       "Symbol": "Eu", 
                       "Element": "Europium", 
                       "Atomic Number": 63, 
                       "Boiling Point": 1802.0, 
                       "Atomic Radius": 231.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Gd": {
                       "Electronegativity": 1.2, 
                       "Group": 0, 
                       "Melting Point": 1585.0, 
                       "Weight": 157.25, 
                       "Density": 7.895, 
                       "Symbol": "Gd", 
                       "Element": "Gadolinium", 
                       "Atomic Number": 64, 
                       "Boiling Point": 3546.0, 
                       "Atomic Radius": 233.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3
                       ]
                   }, 
                   "Tb": {
                       "Electronegativity": 1.2, 
                       "Group": 0, 
                       "Melting Point": 1629.0, 
                       "Weight": 158.92535, 
                       "Density": 8.229, 
                       "Symbol": "Tb", 
                       "Element": "Terbium", 
                       "Atomic Number": 65, 
                       "Boiling Point": 3503.0, 
                       "Atomic Radius": 225.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Dy": {
                       "Electronegativity": 1.22, 
                       "Group": 0, 
                       "Melting Point": 1680.0, 
                       "Weight": 162.5, 
                       "Density": 8.55, 
                       "Symbol": "Dy", 
                       "Element": "Dysprosium", 
                       "Atomic Number": 66, 
                       "Boiling Point": 2840.0, 
                       "Atomic Radius": 228.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Ho": {
                       "Electronegativity": 1.23, 
                       "Group": 0, 
                       "Melting Point": 1734.0, 
                       "Weight": 164.93032, 
                       "Density": 8.795, 
                       "Symbol": "Ho", 
                       "Element": "Holmium", 
                       "Atomic Number": 67, 
                       "Boiling Point": 2993.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Er": {
                       "Electronegativity": 1.24, 
                       "Group": 0, 
                       "Melting Point": 1802.0, 
                       "Weight": 167.259, 
                       "Density": 9.066, 
                       "Symbol": "Er", 
                       "Element": "Erbium", 
                       "Atomic Number": 68, 
                       "Boiling Point": 3141.0, 
                       "Atomic Radius": 226.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Tm": {
                       "Electronegativity": 1.25, 
                       "Group": 0, 
                       "Melting Point": 1818.0, 
                       "Weight": 168.93421, 
                       "Density": 9.321, 
                       "Symbol": "Tm", 
                       "Element": "Thulium", 
                       "Atomic Number": 69, 
                       "Boiling Point": 2223.0, 
                       "Atomic Radius": 222.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Yb": {
                       "Electronegativity": 1.1, 
                       "Group": 0, 
                       "Melting Point": 1097.0, 
                       "Weight": 173.054, 
                       "Density": 6.965, 
                       "Symbol": "Yb", 
                       "Element": "Ytterbium", 
                       "Atomic Number": 70, 
                       "Boiling Point": 1469.0, 
                       "Atomic Radius": 222.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Lu": {
                       "Electronegativity": 1.27, 
                       "Group": 3, 
                       "Melting Point": 1925.0, 
                       "Weight": 174.9668, 
                       "Density": 9.84, 
                       "Symbol": "Lu", 
                       "Element": "Lutetium", 
                       "Atomic Number": 71, 
                       "Boiling Point": 3675.0, 
                       "Atomic Radius": 217.0, 
                       "Oxidation Number(s)": [
                           3
                       ]
                   }, 
                   "Hf": {
                       "Electronegativity": 1.3, 
                       "Group": 4, 
                       "Melting Point": 2506.0, 
                       "Weight": 178.49, 
                       "Density": 13.31, 
                       "Symbol": "Hf", 
                       "Element": "Hafnium", 
                       "Atomic Number": 72, 
                       "Boiling Point": 4876.0, 
                       "Atomic Radius": 208.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Ta": {
                       "Electronegativity": 1.5, 
                       "Group": 5, 
                       "Melting Point": 3290.0, 
                       "Weight": 180.94788, 
                       "Density": 16.654, 
                       "Symbol": "Ta", 
                       "Element": "Tantalum", 
                       "Atomic Number": 73, 
                       "Boiling Point": 5731.0, 
                       "Atomic Radius": 200.0, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4, 
                           5, 
                           -1
                       ]
                   }, 
                   "W": {
                       "Electronegativity": 2.36, 
                       "Group": 6, 
                       "Melting Point": 3695.0, 
                       "Weight": 183.84, 
                       "Density": 19.25, 
                       "Symbol": "W", 
                       "Element": "Tungsten", 
                       "Atomic Number": 74, 
                       "Boiling Point": 5828.0, 
                       "Atomic Radius": 193.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Re": {
                       "Electronegativity": 1.9, 
                       "Group": 7, 
                       "Melting Point": 3459.0, 
                       "Weight": 186.207, 
                       "Density": 21.02, 
                       "Symbol": "Re", 
                       "Element": "Rhenium", 
                       "Atomic Number": 75, 
                       "Boiling Point": 5869.0, 
                       "Atomic Radius": 188.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           -3, 
                           -1
                       ]
                   }, 
                   "Os": {
                       "Electronegativity": 2.2, 
                       "Group": 8, 
                       "Melting Point": 3306.0, 
                       "Weight": 190.23, 
                       "Density": 22.61, 
                       "Symbol": "Os", 
                       "Element": "Osmium", 
                       "Atomic Number": 76, 
                       "Boiling Point": 5285.0, 
                       "Atomic Radius": 185.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           8, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Ir": {
                       "Electronegativity": 2.2, 
                       "Group": 9, 
                       "Melting Point": 2719.0, 
                       "Weight": 192.217, 
                       "Density": 22.56, 
                       "Symbol": "Ir", 
                       "Element": "Iridium", 
                       "Atomic Number": 77, 
                       "Boiling Point": 4701.0, 
                       "Atomic Radius": 180.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           8, 
                           -3, 
                           -1
                       ]
                   }, 
                   "Pt": {
                       "Electronegativity": 2.28, 
                       "Group": 10, 
                       "Melting Point": 2041.4, 
                       "Weight": 195.084, 
                       "Density": 21.46, 
                       "Symbol": "Pt", 
                       "Element": "Platinum", 
                       "Atomic Number": 78, 
                       "Boiling Point": 4098.0, 
                       "Atomic Radius": 177.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           -2, 
                           -1
                       ]
                   }, 
                   "Au": {
                       "Electronegativity": 2.54, 
                       "Group": 11, 
                       "Melting Point": 1337.33, 
                       "Weight": 196.966569, 
                       "Density": 19.282, 
                       "Symbol": "Au", 
                       "Element": "Gold", 
                       "Atomic Number": 79, 
                       "Boiling Point": 3129.0, 
                       "Atomic Radius": 174.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           3, 
                           5, 
                           -1
                       ]
                   }, 
                   "Hg": {
                       "Electronegativity": 2.0, 
                       "Group": 12, 
                       "Melting Point": 234.43, 
                       "Weight": 200.592, 
                       "Density": 13.5336, 
                       "Symbol": "Hg", 
                       "Element": "Mercury", 
                       "Atomic Number": 80, 
                       "Boiling Point": 629.88, 
                       "Atomic Radius": 171.0, 
                       "Oxidation Number(s)": [
                           1, 
                           2, 
                           4
                       ]
                   }, 
                   "Tl": {
                       "Electronegativity": 1.62, 
                       "Group": 13, 
                       "Melting Point": 577.0, 
                       "Weight": 204.389, 
                       "Density": 11.85, 
                       "Symbol": "Tl", 
                       "Element": "Thallium", 
                       "Atomic Number": 81, 
                       "Boiling Point": 1746.0, 
                       "Atomic Radius": 156.0, 
                       "Oxidation Number(s)": [
                           1, 
                           3, 
                           -1
                       ]
                   }, 
                   "Pb": {
                       "Electronegativity": 1.87, 
                       "Group": 14, 
                       "Melting Point": 600.61, 
                       "Weight": 207.2, 
                       "Density": 11.342, 
                       "Symbol": "Pb", 
                       "Element": "Lead", 
                       "Atomic Number": 82, 
                       "Boiling Point": 2022.0, 
                       "Atomic Radius": 154.0, 
                       "Oxidation Number(s)": [
                           2, 
                           4, 
                           -4
                       ]
                   }, 
                   "Bi": {
                       "Electronegativity": 2.02, 
                       "Group": 15, 
                       "Melting Point": 544.7, 
                       "Weight": 208.9804, 
                       "Density": 9.807, 
                       "Symbol": "Bi", 
                       "Element": "Bismuth", 
                       "Atomic Number": 83, 
                       "Boiling Point": 1837.0, 
                       "Atomic Radius": 143.0, 
                       "Oxidation Number(s)": [
                           1, 
                           3, 
                           5, 
                           -3
                       ]
                   }, 
                   "Po": {
                       "Electronegativity": 2.0, 
                       "Group": 16, 
                       "Melting Point": 527.0, 
                       "Weight": 209.0, 
                       "Density": 9.32, 
                       "Symbol": "Po", 
                       "Element": "Polonium", 
                       "Atomic Number": 84, 
                       "Boiling Point": 1235.0, 
                       "Atomic Radius": 135.0, 
                       "Oxidation Number(s)": [
                           2, 
                           4, 
                           5, 
                           6, 
                           -2
                       ]
                   }, 
                   "At": {
                       "Electronegativity": 2.2, 
                       "Group": 17, 
                       "Melting Point": 575.0, 
                       "Weight": 210.0, 
                       "Density": 7.0, 
                       "Symbol": "At", 
                       "Element": "Astatine", 
                       "Atomic Number": 85, 
                       "Boiling Point": 610.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           1, 
                           3, 
                           5, 
                           7, 
                           -1
                       ]
                   }, 
                   "Rn": {
                       "Electronegativity": 2.2, 
                       "Group": 18, 
                       "Melting Point": 202.0, 
                       "Weight": 222.0, 
                       "Density": 0.00973, 
                       "Symbol": "Rn", 
                       "Element": "Radon", 
                       "Atomic Number": 86, 
                       "Boiling Point": 211.3, 
                       "Atomic Radius": 120.0, 
                       "Oxidation Number(s)": [
                           2, 
                           6
                       ]
                   }, 
                   "Fr": {
                       "Electronegativity": 0.7, 
                       "Group": 1, 
                       "Melting Point": 300.0, 
                       "Weight": 223.0, 
                       "Density": 1.87, 
                       "Symbol": "Fr", 
                       "Element": "Francium", 
                       "Atomic Number": 87, 
                       "Boiling Point": 950.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           1
                       ]
                   }, 
                   "Ra": {
                       "Electronegativity": 0.9, 
                       "Group": 2, 
                       "Melting Point": 973.0, 
                       "Weight": 226.0, 
                       "Density": 5.5, 
                       "Symbol": "Ra", 
                       "Element": "Radium", 
                       "Atomic Number": 88, 
                       "Boiling Point": 2010.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2
                       ]
                   }, 
                   "Ac": {
                       "Electronegativity": 1.1, 
                       "Group": 0, 
                       "Melting Point": 1323.0, 
                       "Weight": 227.0, 
                       "Density": 10.07, 
                       "Symbol": "Ac", 
                       "Element": "Actinium", 
                       "Atomic Number": 89, 
                       "Boiling Point": 3471.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Th": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 2115.0, 
                       "Weight": 232.03806, 
                       "Density": 11.72, 
                       "Symbol": "Th", 
                       "Element": "Thorium", 
                       "Atomic Number": 90, 
                       "Boiling Point": 5061.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Pa": {
                       "Electronegativity": 1.5, 
                       "Group": 0, 
                       "Melting Point": 1841.0, 
                       "Weight": 231.03588, 
                       "Density": 15.37, 
                       "Symbol": "Pa", 
                       "Element": "Protactinium", 
                       "Atomic Number": 91, 
                       "Boiling Point": 4300.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4, 
                           5
                       ]
                   }, 
                   "U": {
                       "Electronegativity": 1.38, 
                       "Group": 0, 
                       "Melting Point": 1405.3, 
                       "Weight": 238.02891, 
                       "Density": 18.95, 
                       "Symbol": "U", 
                       "Element": "Uranium", 
                       "Atomic Number": 92, 
                       "Boiling Point": 4404.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4, 
                           5, 
                           6
                       ]
                   }, 
                   "Np": {
                       "Electronegativity": 1.36, 
                       "Group": 0, 
                       "Melting Point": 917.0, 
                       "Weight": 237.0, 
                       "Density": 20.45, 
                       "Symbol": "Np", 
                       "Element": "Neptunium", 
                       "Atomic Number": 93, 
                       "Boiling Point": 4273.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           3, 
                           4, 
                           5, 
                           6, 
                           7
                       ]
                   }, 
                   "Pu": {
                       "Electronegativity": 1.28, 
                       "Group": 0, 
                       "Melting Point": 912.5, 
                       "Weight": 244.0, 
                       "Density": 19.84, 
                       "Symbol": "Pu", 
                       "Element": "Plutonium", 
                       "Atomic Number": 94, 
                       "Boiling Point": 3501.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           3, 
                           4, 
                           5, 
                           6, 
                           7, 
                           8
                       ]
                   }, 
                   "Am": {
                       "Electronegativity": 1.13, 
                       "Group": 0, 
                       "Melting Point": 1449.0, 
                       "Weight": 243.0, 
                       "Density": 13.69, 
                       "Symbol": "Am", 
                       "Element": "Americium", 
                       "Atomic Number": 95, 
                       "Boiling Point": 2880.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4, 
                           5, 
                           6, 
                           7
                       ]
                   }, 
                   "Cm": {
                       "Electronegativity": 1.28, 
                       "Group": 0, 
                       "Melting Point": 1613.0, 
                       "Weight": 247.0, 
                       "Density": 13.51, 
                       "Symbol": "Cm", 
                       "Element": "Curium", 
                       "Atomic Number": 96, 
                       "Boiling Point": 3383.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4, 
                           6, 
                           8
                       ]
                   }, 
                   "Bk": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1259.0, 
                       "Weight": 247.0, 
                       "Density": 14.79, 
                       "Symbol": "Bk", 
                       "Element": "Berkelium", 
                       "Atomic Number": 97, 
                       "Boiling Point": 2900.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Cf": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1173.0, 
                       "Weight": 251.0, 
                       "Density": 15.1, 
                       "Symbol": "Cf", 
                       "Element": "Californium", 
                       "Atomic Number": 98, 
                       "Boiling Point": 1743.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Es": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1133.0, 
                       "Weight": 252.0, 
                       "Density": 8.84, 
                       "Symbol": "Es", 
                       "Element": "Einsteinium", 
                       "Atomic Number": 99, 
                       "Boiling Point": 1269.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3, 
                           4
                       ]
                   }, 
                   "Fm": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1125.0, 
                       "Weight": 257.0, 
                       "Density": None, 
                       "Symbol": "Fm", 
                       "Element": "Fermium", 
                       "Atomic Number": 100, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Md": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1100.0, 
                       "Weight": 258.0, 
                       "Density": None, 
                       "Symbol": "Md", 
                       "Element": "Mendelevium", 
                       "Atomic Number": 101, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "No": {
                       "Electronegativity": 1.3, 
                       "Group": 0, 
                       "Melting Point": 1100.0, 
                       "Weight": 259.0, 
                       "Density": None, 
                       "Symbol": "No", 
                       "Element": "Nobelium", 
                       "Atomic Number": 102, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           2, 
                           3
                       ]
                   }, 
                   "Lr": {
                       "Electronegativity": 1.3, 
                       "Group": 3, 
                       "Melting Point": 1900.0, 
                       "Weight": 262.0, 
                       "Density": None, 
                       "Symbol": "Lr", 
                       "Element": "Lawrencium", 
                       "Atomic Number": 103, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           3
                       ]
                   }, 
                   "Rf": {
                       "Electronegativity": None, 
                       "Group": 4, 
                       "Melting Point": 2400.0, 
                       "Weight": 267.0, 
                       "Density": 23.2, 
                       "Symbol": "Rf", 
                       "Element": "Rutherfordium", 
                       "Atomic Number": 104, 
                       "Boiling Point": 5800.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           4
                       ]
                   }, 
                   "Db": {
                       "Electronegativity": None, 
                       "Group": 5, 
                       "Melting Point": None, 
                       "Weight": 268.0, 
                       "Density": 29.3, 
                       "Symbol": "Db", 
                       "Element": "Dubnium", 
                       "Atomic Number": 105, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           5
                       ]
                   }, 
                   "Sg": {
                       "Electronegativity": None, 
                       "Group": 6, 
                       "Melting Point": None, 
                       "Weight": 269.0, 
                       "Density": 35.0, 
                       "Symbol": "Sg", 
                       "Element": "Seaborgium", 
                       "Atomic Number": 106, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           6
                       ]
                   }, 
                   "Bh": {
                       "Electronegativity": None, 
                       "Group": 7, 
                       "Melting Point": None, 
                       "Weight": 270.0, 
                       "Density": 37.1, 
                       "Symbol": "Bh", 
                       "Element": "Bohrium", 
                       "Atomic Number": 107, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           7
                       ]
                   }, 
                   "Hs": {
                       "Electronegativity": None, 
                       "Group": 8, 
                       "Melting Point": None, 
                       "Weight": 269.0, 
                       "Density": 40.7, 
                       "Symbol": "Hs", 
                       "Element": "Hassium", 
                       "Atomic Number": 108, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           8
                       ]
                   }, 
                   "Mt": {
                       "Electronegativity": None, 
                       "Group": 9, 
                       "Melting Point": None, 
                       "Weight": 278.0, 
                       "Density": 37.4, 
                       "Symbol": "Mt", 
                       "Element": "Meitnerium", 
                       "Atomic Number": 109, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": [
                           8
                       ]
                   }, 
                   "Ds": {
                       "Electronegativity": None, 
                       "Group": 10, 
                       "Melting Point": None, 
                       "Weight": 281.0, 
                       "Density": 34.8, 
                       "Symbol": "Ds", 
                       "Element": "Darmstadtium", 
                       "Atomic Number": 110, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Rg": {
                       "Electronegativity": None, 
                       "Group": 11, 
                       "Melting Point": None, 
                       "Weight": 281.0, 
                       "Density": 28.7, 
                       "Symbol": "Rg", 
                       "Element": "Roentgenium", 
                       "Atomic Number": 111, 
                       "Boiling Point": None, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Cn": {
                       "Electronegativity": None, 
                       "Group": 12, 
                       "Melting Point": None, 
                       "Weight": 285.0, 
                       "Density": 23.7, 
                       "Symbol": "Cn", 
                       "Element": "Copernicium", 
                       "Atomic Number": 112, 
                       "Boiling Point": 357.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Uut": {
                       "Electronegativity": None, 
                       "Group": 13, 
                       "Melting Point": 700.0, 
                       "Weight": 286.0, 
                       "Density": 16.0, 
                       "Symbol": "Uut", 
                       "Element": "Ununtrium", 
                       "Atomic Number": 113, 
                       "Boiling Point": 1400.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Fl": {
                       "Electronegativity": None, 
                       "Group": 14, 
                       "Melting Point": 340.0, 
                       "Weight": 289.0, 
                       "Density": 14.0, 
                       "Symbol": "Fl", 
                       "Element": "Flerovium", 
                       "Atomic Number": 114, 
                       "Boiling Point": 420.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Uup": {
                       "Electronegativity": None, 
                       "Group": 15, 
                       "Melting Point": 700.0, 
                       "Weight": 288.0, 
                       "Density": 13.5, 
                       "Symbol": "Uup", 
                       "Element": "Ununpentium", 
                       "Atomic Number": 115, 
                       "Boiling Point": 1400.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Lv": {
                       "Electronegativity": None, 
                       "Group": 16, 
                       "Melting Point": 708.5, 
                       "Weight": 293.0, 
                       "Density": 12.9, 
                       "Symbol": "Lv", 
                       "Element": "Livermorium", 
                       "Atomic Number": 116, 
                       "Boiling Point": 1085.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Uus": {
                       "Electronegativity": None, 
                       "Group": 17, 
                       "Melting Point": 673.0, 
                       "Weight": 294.0, 
                       "Density": 7.2, 
                       "Symbol": "Uus", 
                       "Element": "Ununseptium", 
                       "Atomic Number": 117, 
                       "Boiling Point": 823.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }, 
                   "Uuo": {
                       "Electronegativity": None, 
                       "Group": 18, 
                       "Melting Point": 258.0, 
                       "Weight": 294.0, 
                       "Density": 5.0, 
                       "Symbol": "Uuo", 
                       "Element": "Ununoctium", 
                       "Atomic Number": 118, 
                       "Boiling Point": 263.0, 
                       "Atomic Radius": None, 
                       "Oxidation Number(s)": None
                   }
               }
