from BaseInventoryManagement import InventoryItem

class RegularItem(InventoryItem):
    print("Regular Item")



class PerishableItem(InventoryItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def __str__(self):
        return f'{self.name} (Expires: {self.expiry_date}): {self.quantity}'

