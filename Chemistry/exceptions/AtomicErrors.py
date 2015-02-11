# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


class AtomicError(Exception):
    """A generic error to be thrown if there is an issue regarding atoms.

    Parameters
    ----------
    message : string
        The error message.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return str(self)


class ValenceError(AtomicError):
    """Error to be thrown if there is an issue regarding the valence of an atom.

    Parameters
    ----------
    atom : Atom
        The atom whose valence is being violated.
    """

    def __init__(self, atom):
        message = "A {} atom has a valence number of {}".format(
            atom.name, atom.valence)
        super(ValenceError, self).__init__(message)
