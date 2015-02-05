# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Errors associated with chemical reactions."""

__author__ = "Dan Obermiller"


class ReactionError(Exception):
    """A generic error to be thrown when there is an error with a reaction
    that does not have any specific error to be thrown.
    """

    err_message = "There was an error with the reaction"
    pka = """
    AcidBase reaction between {} and {} failed because of pka difference {}
    ({} to {})
    """

    def __init__(self, message=None, **kwargs):
        if message:
            self.err_message = message
        elif 'pka' in kwargs:
            self.err_message = ReactionError.pka.format(*kwargs['reactants']
                                                        *kwargs['pka'])

    def __str__(self):
        return self.err_message

    def __repr__(self):
        return str(self)
        

class NoReactionError(ReactionError):
    """A specific reaction error that should be thrown if the given scenario
    would not give rise to that specific type of reaction.

    Parameters
    ----------
    msg : string, optional
        The error message.
    """

    err_message = "No reaction occurred"
    
    def __init__(self, msg=err_message):
        super(NoReactionError, self).__init__(msg)
