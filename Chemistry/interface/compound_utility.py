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

from Chemistry.base.compounds import Compound
from Chemistry.parsing.CheML import CMLParser, CMLBuilder
from Chemistry.parsing.mol.molv2000 import MolV2000Parser, MolV2000Builder
from Chemistry.parsing.mol.molv3000 import MolV3000Parser, MolV3000Builder


SUPPORTED_FILETYPES = {'cml': [CMLParser, CMLBuilder],
                       'molv2000': [MolV2000Parser, MolV2000Builder],
                       'molv3000': [MolV3000Parser, MolV3000Builder]}


def compound_from_dict(atoms, bonds, other):
    """Builds a compound from dictionaries representing the atoms, bonds, and
    other necessary information.

    Parameters
    ----------
    atoms : dict
        Dictionary storing all of the atomic information.  Should be in form
        `{'a1': 'H', 'a2': 'O', 'a3': 'H'}`.
    bonds : dict
        Dictionary storing all of the bond information.  Should be in form
        `{'b1': ('a1', 'a2', {'order': 1}), 'b2': ('a2', 'a3', {'order': 1})}`.
    other : dict
        Dictionary storing any other available information about the molecule.

    Returns
    -------
    Compound
        The compound object that stores all of this information.

    Notes
    -----
    - The `other` dictionary can have a lot of information.  For example, data
    necessary to write the data to a specific filetype.  This should be stored
    as something like `cml`: {information necessary}.  Certain assumptions
    are/will be made by the API and will be documented as necessary.
    - This function is a thin wrapper for the Compound constructor.
    """

    return Compound(atoms, bonds, other)


def compound_to_dict(compound):
    """Generates a dictionary that can store relevant compound information.

    Parameters
    ----------
    compound : Compound
        The compound to be turned into a dict

    Returns
    -------
    dict
        A three item dictionary of form {'atoms': info, 'bonds': info,
        'other': info}.
    """

    return {'atoms': compound.atoms,
            'bonds': compound.bonds,
            'other': compound.other_info}


def compound_from_file(file_, filetype):
    """Builds a compound object from file.

    Parameters
    ----------
    file_ : file-like object
        The (open) file-like object from which data can be read and parsed.
    filetype : string
        The type of file that is being parsed.  This should be one of the keys
        of the SUPPORTED_FILETYPES constant.

    Returns
    -------
    Compound
        The `Compound` object that can be generated from the file.

    Raises
    ------
    ValueError
        Raised if the filetype given is not supported.
    """

    try:
        return SUPPORTED_FILETYPES[filetype][0](file_)
    except KeyError:
        raise ValueError("{} is not a supported filetype".format(filetype))


def compound_to_file(file_, filetype, compound):
    """Writes a compound object to a file.

    Parameters
    ----------
    file_ : file-like object
        The (open) file to which the compound information will be written.
    filetype : string
        The type of file that is being parsed.  This should be one of the keys
        of the SUPPORTED_FILETYPES constant.
    compound : Compound
        The compound being written to file.

    Raises
    ------
    ValueError
        Raised if the filetype given is not supported.
    """

    try:
        return SUPPORTED_FILETYPES[filetype][1](file_, compound)
    except KeyError:
        raise ValueError("{} is not a supported filetype".format(filetype))
