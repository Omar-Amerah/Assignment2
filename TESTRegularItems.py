import unittest

from RegularItems import RegularItem, PerishableItem, AgeRestrictedItem, FragileItem


class RegularItems(unittest.TestCase):

    def setUp(self):
        self.regular_item = RegularItem("Phone", 10)
        self.perishable_item = PerishableItem("Phone", 10, 12/12/2024)
        self.age_restricted_item = AgeRestrictedItem("Phone", 10, 16)
        self.fragile_item = FragileItem("Phone", 10, True)

    def test_get_expiry(self):
        expiry = self.perishable_item.get_details()

        self.assertEqual(expiry, 12/12/2024)

    def test_get_age(self):
        age = self.age_restricted_item.get_details()

        self.assertEqual(age, 16)

    def test_get_fragility(self):
        fragility = self.fragile_item.get_details()

        self.assertEqual(fragility, True)

