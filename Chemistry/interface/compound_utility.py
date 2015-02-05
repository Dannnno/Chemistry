# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Provides a public API for creating molecules from various sources, and
converting Compound objects back into file or dictionaries.
"""

__author__ = "Dan Obermiller"


from Chemistry.base.compounds import Compound
from Chemistry.parsing.CheML import CMLParser, CMLBuilder
from Chemistry.exceptions.ParseErrors import UnsupportedFileTypeException


SUPPORTED_FILETYPES = {'cml': [CMLParser, CMLBuilder]}


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


def _parser_to_compound(parsed_file):
    """Takes the result of parsing a file and turns it into a compound object.

    Parameters
    ----------
    parsed_file : some parser object
        The parser object that has already parsed a molecular file.

    Returns
    -------
    Compound
        The resulting compound.
    """

    return Compound(parsed_file.atoms, parsed_file.bonds, parsed_file.other)

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
    UnsupportedFiletypeException
        Raised if the filetype given is not supported.
    """

    try:
        return _parser_to_compound(SUPPORTED_FILETYPES[filetype][0](file_))
    except KeyError:
        raise UnsupportedFileTypeException(filetype, "Unsupported filetype {}")


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
    UnsupportedFiletypeException
        Raised if the filetype given is not supported.
    """

    try:
        SUPPORTED_FILETYPES[filetype][1].from_compound(compound).to_file(file_)
    except KeyError:
        raise UnsupportedFileTypeException(filetype, "Unsupported filetype {}")
