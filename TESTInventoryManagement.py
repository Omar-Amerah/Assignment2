import unittest

from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem

class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()

    def test_add_section(self):
        section = InventorySection("Electronics")
        self.inventory_manager.add_section(section)

        self.assertIn("Electronics", self.inventory_manager.sections)

    def test_get_section(self):
        section = InventorySection("Electronics")
        self.inventory_manager.add_section(section)
        returned_section = self.inventory_manager.get_section("Electronics")

        self.assertEqual(returned_section, section)

    def test_add_item(self):
        section = InventorySection("Electronics")
        item = RegularItem("Phone", 10)


        self.inventory_manager.add_section(section)
        self.inventory_manager.add_item("Electronics", item)

        self.assertIn("Phone", section.items)

    def test_get_items_in_section(self):
        section = InventorySection("Electronics")
        item_1 = RegularItem("Phone", 10)
        item_2 = RegularItem("Laptop", 10)

        self.inventory_manager.add_section(section)
        self.inventory_manager.add_item("Electronics", item_1)
        self.inventory_manager.add_item("Electronics", item_2)

        returned_item = self.inventory_manager.get_items_in_section("Electronics")

        self.assertEqual(len(returned_item), 2)
        self.assertIn("Phone", section.items)
        self.assertIn("Laptop", section.items)

    def test_add_stock(self):
        section = InventorySection("Electronics")
        item = RegularItem("Phone", 10)

        self.inventory_manager.add_section(section)
        self.inventory_manager.add_item("Electronics", item)

        self.inventory_manager.add_stock("Electronics", item.name, 15)

        self.assertEqual(item.quantity, 25)


    def test_remove_stock(self):
        section = InventorySection("Electronics")
        item = RegularItem("Phone", 10)

        self.inventory_manager.add_section(section)
        self.inventory_manager.add_item("Electronics", item)

        self.inventory_manager.remove_stock("Electronics", item.name, 5)

        self.assertEqual(item.quantity, 5)

    def test_move_stock(self):
        section_1 = InventorySection("Electronics")
        section_2 = InventorySection("Automotive")
        item = RegularItem("Phone", 20)

        self.inventory_manager.add_section(section_1)
        self.inventory_manager.add_section(section_2)
        self.inventory_manager.add_item("Electronics", item)

        self.inventory_manager.move_stock(section_1.name, section_2.name, item.name, 10)

        self.assertIn("Phone", section_2.items)
        self.assertEqual(section_1.get_item("Phone").quantity, 10)
        self.assertEqual(section_2.get_item("Phone").quantity, 10)


    def test_get_inventory(self):
        section_1 = InventorySection("Electronics")
        section_2 = InventorySection("Automotive")

        self.inventory_manager.add_section(section_1)
        self.inventory_manager.add_section(section_2)

        returned_invtentory = self.inventory_manager.get_inventory()
        print(returned_invtentory)
        self.assertEqual(returned_invtentory, ["Electronics", "Automotive"])

