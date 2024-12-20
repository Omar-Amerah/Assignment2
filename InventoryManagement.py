class InventoryManager:
    def __init__(self):
        self.sections = {}

    def add_section(self, section):
        self.sections[section.get_name()] = section

    def get_section(self, name):
        return self.sections.get(name)

    def add_item(self, section_name, item):
        section = self.get_section(section_name)
        if section:
            section.add_item(item)
        else:
            raise ValueError("Section not found")

    def get_items_in_section (self, section_name) :
        section = self.get_section(section_name)
        if section:
            return [str(item) for item in section.items.values()]
        return []

    def add_stock(self, section_name, name, amount, misc_info = "a"):
        section = self.get_section(section_name)
        if section:
            section.add_stock(name, amount, misc_info)
        else:
            raise ValueError("Section not found")

    def remove_stock(self, section_name, name, amount):
        section = self.get_section(section_name)
        if section:
            try:
                section.remove_stock(name, amount)
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Section not found")

    def move_stock(self, from_section_name, to_section_name, item_name, amount):
        from_section = self.get_section(from_section_name)
        to_section = self.get_section(to_section_name)
        if from_section and to_section:
            try:
                from_section.remove_stock(item_name, amount)
                to_section.add_stock(item_name, amount, "m")
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Section(s) not found")

    def get_inventory(self):
        inventory = []
        for section in self.sections.values():
            inventory.append(str(section.get_name()))
            inventory.extend(str(item) for item in section.items.values())
        return inventory