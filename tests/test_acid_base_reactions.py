# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import unittest

from Chemistry.base.compounds import Compound
from Chemistry.base.reactants import Acid, Base
from Chemistry.base.products import Product, Products
from Chemistry.reactions._reactions import Conditions
from Chemistry.reactions.acid_base import AcidBase
from Chemistry.exceptions.ReactionErrors import NoReactionError


# Todo: Split this up into unique tests for each type of conditions
class TestAcidBaseClass(unittest.TestCase):

    def setUp(self):
        self.compound1 = Compound(
            {"a1": "H", "a2": "H", "a3": "O"},
            {"b1": ("a1", "a3", {'order': 1, 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1, 'chirality': None})},
            {"id": "Water"}
        )
        self.compound2 = Compound(
            {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
            {"b1": ("a1", "a3", {'order': 1, 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1, 'chirality': None}),
             "b3": ("a3", "a4", {'order': 1, 'chirality': None})},
            {"id": "Hydronium"}
        )
        self.hydroiodic = Acid(Compound(
            {"a1": "H", "a2":"I"},
            {"b1": ("a1", "a2", {'order': 1, 'chirality': None})},
            {"id": "Hydroiodic acid"}), 'a1', -10
        )
        self.hydroxide = Base(Compound(
            {"a1": "H", "a2": "O", "a3": "Na"},
            {"b1": ("a1", "a2", {'order': 1, 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1, 'chirality': None})},
            {"id": "Sodium Hydroxide"}), 'a2', 15.7
        )

    def test_constructor_not_raises_TE1(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        AcidBase(acid, base, {})

    def test_constructor_not_raises_TE2(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        AcidBase(acid, base, Conditions({}))

    def test_constructor_raises_TE(self):
        with self.assertRaises(TypeError):
            AcidBase(self.compound2, self.compound1, [])

    def test_get_acid1(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        rxn = AcidBase(acid, base, Conditions({}))
        self.assertEqual(rxn.acid, (acid, 'a1'))

    def test_get_acid2(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        cond = Conditions(
            {'pka': -10, 'acidic': True,
             'pka_molecule': self.hydroiodic,
             'pka_location': 'a1'}
        )
        rxn = AcidBase(acid, base, cond)
        self.assertEqual(
            rxn.acid, (cond.pka_molecule, 'a1')
        )

    def test_get_base1(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        rxn = AcidBase(acid, base, {})
        self.assertEqual(rxn.base, (base, 'a2'))

    def test_get_base2(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        cond = Conditions(
            {'pka': 15.7, 'basic': True,
             'pka_molecule': self.hydroxide,
             'pka_location': 'a2'}
        )
        rxn = AcidBase(acid, base, cond)
        self.assertEqual(
            rxn.base, (cond.pka_molecule, 'a2')
        )

    def test_equilibrium1(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        cond = Conditions({})
        rxn = AcidBase(acid, base, cond)
        with self.assertRaises(NoReactionError):
            rxn._equilibrium()

    def test_equilibrium2(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        cond = Conditions(
            {'pka': -10, 'acidic': True,
             'pka_molecule': self.hydroiodic,
             'pka_location': 'a1'}
        )
        rxn = AcidBase(acid, base, cond)
        self.assertEqual((10**8.26, 1), rxn._equilibrium())

    def test_equilibrium3(self):
        acid = Acid(
            self.compound2, 'a1', -1.74
        )
        base = Base(
            self.compound1, 'a2', -1.74
        )
        cond = Conditions(
            {'pka': 15.7, 'basic': True,
             'pka_molecule': self.hydroxide,
             'pka_location': 'a2'}
        )
        rxn = AcidBase(acid, base, cond)
        self.assertEqual((1, 0), rxn._equilibrium())


class TestAcidBaseReaction(unittest.TestCase):

    def test_hydroxide_hydronium(self):
        hydroxide = Base(Compound(
            {"a1": "H", "a2": "O"},
            {"b1": ("a1", "a2", {'order': 1, 'chirality': None})},
            {"id": "Hydroxide"}), 'a2', 15.7
        )
        hydronium = Acid(Compound(
            {"a1": "H", "a2": "H", "a3": "O", "a4": "H"},
            {"b1": ("a1", "a3", {'order': 1, 'chirality': None}),
             "b2": ("a2", "a3", {'order': 1, 'chirality': None}),
             "b3": ("a3", "a4", {'order': 1, 'chirality': None})},
            {"id": "Hydronium"}), 'a1', -1.74
        )
        conditions = Conditions({})
        reaction = AcidBase(hydronium, hydroxide, conditions)
        actual_products = reaction.react()
        expected_major_products = (
            Product(Compound(
                {"a1": "H", "a2": "O", "a3": "H"},
                {"b1": ("a1", "a2", {'order': 1, 'chirality': None}),
                 "b2": ("a2", "a3", {'order': 1, 'chirality': None})},
                {"id": "Conjugate acid of Hydroxide"}), 50
            ),
            Product(Compound(
                {"a1": "H", "a2": "O", "a3": "H"},
                {"b1": ("a1", "a2", {'order': 1, 'chirality': None}),
                 "b2": ("a2", "a3", {'order': 1, 'chirality': None})},
                {"id": "Conjugate base of Hydronium"}), 50
            )
        )
        expected_minor_products = ()
        expected_products = Products(
            expected_major_products, expected_minor_products
        )

        self.assertEqual(expected_products.major, actual_products.major)
        self.assertEqual(expected_products.minor, actual_products.minor)
