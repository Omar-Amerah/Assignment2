from AdditionalSections import RefrigeratedSection, RestrictedAccessSection
from InventoryManagement import InventoryManager
from RegularItems import RegularItem, PerishableItem, AgeRestrictedItem

import unittest


class TestSections(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.refSection = RefrigeratedSection("Dairy", -10)
        self.resSection = RestrictedAccessSection("Alcoholic Drinks", 18)
        self.inventory_manager.add_section(self.refSection)
        self.inventory_manager.add_section(self.resSection)

    def test_refrigerated_add_item_successful(self):
        item = PerishableItem("Milk", 10, 11/12/2024)

        self.refSection.add_item(item)

        self.assertIn("Milk", self.refSection.items)

    def test_restricted_add_item_successful(self):
        item = AgeRestrictedItem("Orange Juice", 10, 18)

        self.resSection.add_item(item)

        self.assertIn("Orange Juice", self.resSection.items)

