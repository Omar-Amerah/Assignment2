import unittest

from BaseInventoryManagement import InventoryItem

class TestBaseInventoryItem(unittest.TestCase):

    def setUp(self):
        self.inventory_item = InventoryItem("Phone", 10)


    def test_add_item(self):
        self.inventory_item.add_stock(10)

        self.assertEqual(self.inventory_item.quantity, 20)

    def test_remove_item(self):
        self.inventory_item.remove_stock(5)

        self.assertEqual(self.inventory_item.quantity, 5)