#Abstraction: Define abstract base class for a generic inventory item
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= amount

    def __str__(self):
        return f'{self.name}: {self.quantity}'

