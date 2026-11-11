
class Item:

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

class Inventory:

    def __init__(self):
        self.inventory = dict()
    
    def add_to_inventory(self, item):
        name = item.name
        if name in self.inventory:
            self.inventory[name].qty += item.qty
        else:
            self.inventory[name] = item

    def get_number_items(self):
        total = 0
        for item in self.inventory.values():
            total += item.qty
        return total

if __name__ == "__main__":
    potato = Item('Potato', 3, 1.0)
    potato2 = Item('Potato', 4, 1.0)
    inv = Inventory()
    inv.add_to_inventory(potato2)
    inv.add_to_inventory(potato)

    print(inv.get_number_items())