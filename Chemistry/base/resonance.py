# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Tools necessary to determine the resonance struture(s) of a compound.

Resonance is when a molecule has multiple electron configurations that each
contribute to the "actual" electron distribution of the molecule.  This is seen
most strongly in aromatic compounds.  Consider the following group of atoms in a
compound.

    'a1': 'H', 'a2': 'H', 'a3': 'H',
    'a4': 'C', 'a5': 'C',
    'a6': 'O',  'a7': 'O'

This has two different possible bond configurations.

    'b1': ('a1', 'a4', {'order': 1}), 'b2': ('a2', 'a4', {'order': 1}),
    'b3': ('a3', 'a4', {'order': 1}), 'b4': ('a4', 'a5', {'order': 1})

The above section is the same in either configuration.  Below, however, there
can be two different arrangements that are equally likely.

    'b5': ('a5', 'a6', {'order': 2}), 'b6': ('a5', 'a7', {'order': 1})
or
    'b5': ('a5', 'a6', {'order': 1}), 'b6': ('a5', 'a7', {'order': 2})

This can be visualized in a system such as

          O-                      O
          |                       ||   _
    CH3 - C = O     or      CH3 - C - O

Both of these possible structures contribute equally to the actual structure of
the molecule.  Thus, this molecule exhibits resonance.  Resonance is a key
factor in many reactions.

In general, resonance can be determined by following a number of rules, given
here in the (approximate) order in which they should be followed.

    1. Octet rule trumps.
        Compounds favor arrangements that conform to the octet rule (except for
        centers that can have expanded octets).  Except for those centers, all
        structures must meet the octet rule.
    2. Separation of formal charge should be avoided.
        While formal charge is inevitable in some cases, it is better to have
        charges closer together.
    3. Formal charge is to be avoided.
        The example structure above has a negative charge on it, located on the
        two Oxygen atoms (or more accurately shared between them).  This formal
        charge is unavoidable, however in other structures there will be
        arrangements that have more (or less) atoms exhibiting formal charge.
    4. There must be driving force.
        There must be a reason for the electrons to move.  This all comes down
        to more favorable energy states.
    5. sp3 hybridized atoms are off-limits for resonance
        They don't have the open p-orbital necessary for resonance to occur.
    6. Lone pairs can't jump atoms, but pi-bonds can.
        Lone pair electrons move from bond to atom to bond, while a pi-bond can
        jump to the other side of one of its nodes.
"""

__author__ = 'Dan Obermiller'


def get_resonance_structures(compound):
    """Returns a list of resonance structures.

    Parameters
    ----------
    compound : Compound
        The compound whose resonance structures are being determined.

    Returns
    -------
    structures : list
        The list of resonance structures.  May be empty if there are no such
        structures.
    """

    structures = []

    if not _can_resonate(compound):
        return structures


def _can_resonate(compound):
    """Determines whether or not the compound can even have any resonance
    structures.

    Parameters
    ----------
    compound : Compound
        The compound whose resonance structures are being determined.

    Returns
    -------
    bool
        If the compound can resonate.
    """

    has_available_electrons = _find_available_electrons(compound)
    if not has_available_electrons:
        return False

    all_sp3 = _all_sp3(compound)
    if all_sp3:
        return False

    return True


def _find_available_electrons(compound):
    """Determines whether or not the given compound has any electrons available
    for resonance.

    Parameters
    ----------
    compound : Compound
        The compound whose resonance structures are being determined.

    Returns
    -------
    bool
        If the compound has the necessary electrons or pi-bonds.
    """

    # Return True at the first atom we find with lone pair electrons
    for atom in compound.atoms.itervalues():
        if atom['lpe']:
            return True

    # Return True at the first double or triple bond.
    for _, _, info in compound.bonds.itervalues():
        if info['order'] > 1:
            return True

    return False


def _all_sp3(compound):
    """Determines if a compound consists entirely of sp3 hybridized atoms.

    Parameters
    ----------
    compound : Compound
        The compound being examined.

    Returns
    -------
    bool
        If the compound has at least 2 non-sp3 atoms.
    """

    first = False

    for atom in compound.atoms.itervalues():
        if first and atom['hybrid'] != 'sp3':
            return True
        elif atom['hybrid'] != 'sp3':
            first = True

    return False
