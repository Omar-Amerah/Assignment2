import unittest

from BaseInventoryItem import InventoryItem

class TestBaseInventoryItem(unittest.TestCase):

    def setUp(self):
        self.inventory_item = InventoryItem("Phone", 10)

    def test_get_name(self):
        name = self.inventory_item.get_name()

        self.assertEqual(name, "Phone")

    def test_get_quantity(self):
        quantity = self.inventory_item.get_quantity()

        self.assertEqual(quantity, 10)

    def test_add_item(self):
        self.inventory_item.add_stock(10)

        self.assertEqual(self.inventory_item.get_quantity(), 20)

    def test_remove_item(self):
        self.inventory_item.remove_stock(5)

        self.assertEqual(self.inventory_item.get_quantity(), 5)