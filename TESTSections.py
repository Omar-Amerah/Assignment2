import unittest
from unittest.mock import patch
from tkinter import messagebox

from InventoryManagement import InventoryManager
from BaseSections import InventorySection
from RegularItems import RegularItem, FragileItem

class TestSections(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.section = InventorySection("Electronics")
        self.inventory_manager.add_section(self.section)

    def test_add_item_regular(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)

        self.assertIn("Phone", self.section.items)

    def test_add_item_fragile(self):
        item = FragileItem("Phone", 10, True)

        self.section.add_item(item)

        self.assertIn("Phone", self.section.items)


    def test_get_item(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        returned_item = self.section.get_item(item.get_name())

        self.assertEqual(returned_item.get_name(), "Phone")
        self.assertEqual(returned_item.get_quantity(), 10)

    def test_add_stock(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        self.section.add_stock(item.get_name(), 10)

        self.assertEqual(item.get_quantity(), 20)


    def test_remove_stock(self):
        item = RegularItem("Phone", 10)

        self.section.add_item(item)
        self.section.remove_stock(item.get_name(), 5)

        self.assertEqual(item.get_quantity(), 5)
