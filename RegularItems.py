from BaseInventoryItem import InventoryItem
class RegularItem(InventoryItem):
    print("Item created")



class PerishableItem(InventoryItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def get_expiry(self):
        return self.expiry_date

    def __str__(self):
        return f'{self.name} (Expires: {self.expiry_date}): {self.quantity}'


class AgeRestrictedItem(InventoryItem):
    def __init__(self, name, quantity, minimum_age):
        super().__init__(name, quantity)
        self.minimum_age = minimum_age

    def get_age(self):
        return self.minimum_age

    def __str__(self):
        return f'{self.name} (Minimum Age: {self.minimum_age})'

class FragileItem(InventoryItem):
    def __init__(self, name, quantity, is_fragile):
        super().__init__(name, quantity)
        self.is_fragile = is_fragile

    def get_fragility(self):
        return self.is_fragile

    def __str__(self):
        return f'{self.name} (Fragile: {self.is_fragile})'