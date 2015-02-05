# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Specific exceptions and errors raised during the parsing of chemical data
files.  Deprecated, along with the entire Chemistry.parsing package.  Will be
removed once complete support of OpenBabel is achieved.
"""

__author__ = "Dan Obermiller"


class ParsingException(Exception):
    """A generic exception to be thrown if there is an error with the
    parsing of a chemical data file.

    Parameters
    ----------
    filetype : string
        The type of file that was being parsed.
    msg : string, optional
        The error message.  A default message is provided, however an actual
        message is encouraged.
    """

    message = "An error occurred while parsing a {} file"

    def __init__(self, filetype, msg=message):
        self.filetype = filetype
        self.message = msg.format(self.filetype)

    def __str__(self):
        return self.message

    def __repr__(self):
        return str(self)


class UnsupportedFileTypeException(ParsingException):
    """Exception to be raised if a file is supplied for parsing that is not yet
    supported.

    Parameters
    ----------
    msg : string
        The error message.
    filetype : string
        The filetype that is not currently supported.
    """

    def __init__(self, msg, filetype):
        super(UnsupportedFileTypeException, self).__init__(filetype, msg)