# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014 Dan Obermiller
#
# The full license is available in the root directory of the repository

"""Parser and builder for CML files.  On the path to deprecation."""

__author__ = "Dan Obermiller"


import json

from lxml import etree
from lxml import builder as lb


class CMLParser(object):
    """Parser for CML files.

    Parameters
    ----------
    cml_file : file-like object
        The (open) file that contains the data.

    Notes
    -----
    Pretty limited on what it can actually handle; it expects that things are
    formatted the way I do and not more generically.  I want to eventually make
    this more generalizable.
    """

    def __init__(self, cml_file):
        self.cml_file = cml_file
        self.bonds = {}
        self.atoms = {}
        self.other = {}
        self.molecule = {
            'atoms': self.atoms,
            'bonds': self.bonds,
            'other_info': self.other
        }

        self.CML_tree = etree.iterparse(self.cml_file)
        atom, bond = True, False
        last = ''

        # Todo: put this in a method or get rid of this module
        for _, element in self.CML_tree:
            if element.tag == 'molecule':
                self.other.update(dict(element.items()))
            elif element.tag == 'atomArray':
                atom, bond = False, True
                last = []

            elif atom:
                if 'string' in element.tag:
                    last = element.text
                elif 'atom' in element.tag:
                    self.atoms[element.get('id')] = last

            elif bond:
                if 'string' in element.tag:
                    last.append(element.text)
                elif 'bond' in element.tag:
                    self.bonds[element.get('id')] = [part for part in last]
                    last = []

        del self.bonds[None]

        for key, bond in self.bonds.items():
            try:
                rest = bond[2:]
            except KeyError:
                self.bonds[key] = (bond[0], bond[1],
                                   {'order': 1, 'chirality': 'None'},)
            else:
                if len(rest) == 1:
                    self.bonds[key] = (bond[0], bond[1],
                                       {'order': int(rest[0]),
                                        'chirality': 'None'})
                elif len(rest) == 2:
                    self.bonds[key] = (bond[0], bond[1],
                                       {'order': int(rest[0]),
                                        'chirality': rest[1]})
                else:
                    d = {'order': int(rest[0]),
                         'chirality': rest[1]}
                    i = 0
                    for value in rest[2:]:
                        d['unknown{}'.format(i)] = '{}'.format(value)
                        i += 1
                    self.bonds[key] = (bond[0], bond[1], d)
            if self.bonds[key][2]['chirality'] == 'None':
                self.bonds[key][2]['chirality'] = None

    def __str__(self):
        return json.dumps(self.molecule, indent=4)


class CMLBuilder(object):
    """Object used to build a CML file.

    Parameters
    ----------
    molecule_dict : dict
        Dictionary storing all of the molecular information.
    """

    @classmethod
    def from_compound(cls, comp):
        """Generates a CMLBuilder object from a Compound object.

        Parameters
        ----------
        comp : Compound
            The compound to be written to file.

        Returns
        -------
        CMLBuilder
            The builder object with the relevant information.
        """

        atoms = {}
        bonds = {}

        for key, data in comp.node.iteritems():
            atoms[key] = data['symbol']

        for first, rest in comp.edge.iteritems():
            for second, data in rest.iteritems():
                bond = data['bond_obj']
                bonds.update(
                    {data['key']: (first, second,
                                   {'order': bond.order,
                                    'chirality': str(bond.chirality)})}
                )

        other = {key: str(value) for key, value in comp.other_info.iteritems()}
        m = {'atoms': atoms, 'bonds': bonds, 'other_info': other}
        return CMLBuilder(m)

    def __init__(self, molecule_dict):
        self.atoms = molecule_dict['atoms']
        self.bonds = molecule_dict['bonds']
        self.attribs = molecule_dict['other_info']

        for key, atom in self.atoms.items():
            self.atoms[key] = lb.E.atom(
                lb.E.string(atom, builtin="elementType"), id=key
            )

        for key, bond in self.bonds.items():
            order = str(bond[2]['order'])
            chirality = str(bond[2]['chirality'])
            self.bonds[key] = lb.E.bond(
                lb.E.string(bond[0], builtin="atomRef"),
                lb.E.string(bond[1], builtin="atomRef"),
                lb.E.string(order, builtin="order"),
                lb.E.string(chirality, builtin="chirality"),
                id=key
            )

        self.CML = lb.E.molecule(
            lb.E.atomArray(*sorted(self.atoms.values(),
                                   key=lambda x: x.get('id'))),
            lb.E.bondArray(*sorted(self.bonds.values(),
                                   key=lambda x: x.get('id'))),
            **self.attribs
        )

    def to_file(self, cml_file):
        """Writes the data in the builder object to file.

        Parameters
        ----------
        cml_file : file-like
            The open file to which the compound should be written.
        """

        cml_file.write(str(self))

    def __str__(self):
        return etree.tostring(self.CML, pretty_print=True)

    def __repr__(self):
        return str(self)
