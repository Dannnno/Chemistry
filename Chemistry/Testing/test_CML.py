# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import itertools
import os
import tempfile
import unittest

from Chemistry.interface.compound_utility import compound_from_file
from Chemistry.parsing import CheML as cml


class test_cml_parser(unittest.TestCase):
    primary = os.getcwd()

    def setUp(self):
        os.chdir(os.path.join(self.primary, "Chemistry", "Testing",
                              "test_molecules", "CML"))
        self.molecule = {'atoms': {'a1': 'H',
                                   'a2': 'H',
                                   'a3': 'O'},
                         'bonds': {'b1': ('a1', 'a3', {'order': 1,
                                                       'chirality': None}),
                                   'b2': ('a2', 'a3', {'order': 1,
                                                       'chirality': None})},
                         'other_info': {'id': 'Water'}}

    def test_parse(self):
        with open('CML_1.cml', 'r') as CML_file:
            Parser = cml.CMLParser(CML_file)
        self.assertEqual(Parser.molecule,
                         self.molecule)

    def tearDown(self):
        os.chdir(self.primary)


class test_cml_builder(unittest.TestCase):
    primary = os.getcwd()

    def setUp(self):
        os.chdir(os.path.join(self.primary, "Chemistry", "Testing",
                              "test_molecules", "CML"))
        with open('CML_1.cml', 'r') as cml_file:
            self.molecule = cml.CMLParser(cml_file)
            cml_file.seek(0)
            self.cml = cml_file.read()
        self.Builder1 = cml.CMLBuilder(
                {'atoms': {'a1': 'H',
                           'a2': 'H',
                           'a3': 'O'},
                 'bonds': {'b1': ['a1', 'a3', {'order':1,
                                               'chirality': None}],
                           'b2': ['a2', 'a3', {'order':1,
                                               'chirality': None}]},
                 'other_info': {'id': 'Water'}})
        self.Builder2 = cml.CMLBuilder(self.molecule.molecule)

    def test_to_file(self):
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.cml',
                                         dir=self.primary) as tfile:
            self.Builder1.to_file(tfile)
            tfile.seek(0)
            Builder3 = cml.CMLBuilder(cml.CMLParser(tfile).molecule)
            self.assertEqual(str(self.Builder1), str(Builder3))

    def test_build(self):
        for line1, line2 in itertools.izip(
                                            str(self.Builder1).split('\n'),
                                            self.cml.split('\n')
                                           ):
            self.assertEqual(line1.lstrip(), line2.lstrip())

    def test_from_Compound(self):
        with open("CML_1.cml", 'r') as cml_file:
            builder = cml.CMLBuilder.from_compound(
                compound_from_file(cml_file, 'cml'))

            with tempfile.NamedTemporaryFile(mode='r+',
                                             suffix='.cml',
                                             dir=os.getcwd()
                                             ) as tfile:
                builder.to_file(tfile)
                tfile.seek(0)
                cml_file.seek(0)
                self.assertEqual(
                    compound_from_file(cml_file, 'cml'),
                    compound_from_file(tfile, 'cml'))


if __name__ == '__main__':
    from . import helper
    helper(globals())
