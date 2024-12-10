from BaseSections import InventorySection
from RegularItems import RegularItem, PerishableItem, FragileItem, AgeRestrictedItem
from tkinter import messagebox

class RefrigeratedSection(InventorySection):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def add_item(self, item):
        if not isinstance(item, PerishableItem):
            messagebox.showinfo("WARNING", "Only Perishable Items can be added to Refrigerated Section")
        else:
            self.items[item.get_name()] = item

class RestrictedAccessSection(InventorySection):
    def __init__(self, name, minimum_age):
        super().__init__(name)
        self.minimum_age = minimum_age

    def add_item(self, item):
        if not isinstance(item, AgeRestrictedItem):
            messagebox.showinfo("WARNING", "Only 18+ items can be added to restricted area")
        elif item.get_details() <= self.minimum_age:
            messagebox.showinfo("WARNING", "Only 18+ items can be added to restricted area")
        else:
            self.items[item.get_name()] = item

