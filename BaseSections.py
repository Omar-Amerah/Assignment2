from RegularItems import RegularItem, PerishableItem, FragileItem, AgeRestrictedItem
from tkinter import messagebox

#Encapsulation: Inventory management class that interact with items
class InventorySection:
    def __init__(self, name):
        self._name = name
        self.items = {}

    def get_name(self):
        return self._name

    def add_item(self, item):
        if isinstance(item, FragileItem):
            messagebox.showinfo("WARNING", "This is a Fragile Item")
        if isinstance(item, AgeRestrictedItem):
            messagebox.showinfo("WARNING", "This is a Restricted Item")
        self.items[item.get_name()] = item

    def get_item(self, name):
        return self.items.get(name)

    def add_stock(self, name, amount, misc_info=None, exp_date = None):
        item = self.get_item(name)
        if item:
            item.add_stock(amount)
        else:
            if misc_info == "p":
                item = PerishableItem(name, 0, exp_date)
            else:
                item = RegularItem(name, 0)
            self.add_item(item)
            item.add_stock(amount)

    def remove_stock(self, name, amount):
        item = self.get_item(name)
        if item:
            try:
                item.remove_stock(amount)
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Item not found")

        def __str__(self):
            return f'section: {self.name}'

