class InventoryItem:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def add_stock(self, amount):
        self._quantity += amount

    def remove_stock(self, amount):
        if amount > self.get_quantity():
            raise ValueError("Not enough stock")
        self._quantity -= amount

    def get_details(self):
        raise NotImplementedError("Child class will implement this.")

    def __str__(self):
        return f'{self._name}: {self.get_quantity()}'

