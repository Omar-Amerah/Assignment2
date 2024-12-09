import unittest

from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem

class TestSections(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.section = InventorySection("Electronics")
        self.inventory_manager.add_section(self.section)

    def test_add_item(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)

        self.assertIn("Phone", self.section.items)

    def test_get_item(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        returned_item = self.section.get_item(item.name)

        self.assertEqual(returned_item.name, "Phone")
        self.assertEqual(returned_item.quantity, 10)

    def test_add_stock(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        self.section.add_stock(item.name, 10)

        self.assertEqual(item.quantity, 20)


    def test_remove_stock(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        self.section.remove_stock(item.name, 5)

        self.assertEqual(item.quantity, 5)
