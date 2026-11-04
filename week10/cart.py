
class Cart:

    def __init__(self, owner):
        self.owner = owner
        self.items = {}

    def add_to_cart(self, item_name, value, quantity):
        if item_name in self.items:
            self.items[item_name]['qty'] += quantity          
        else:
            self.items[item_name] = {"value": value, "qty": quantity}

    def sub_total(self):
        total = 0
        for v in self.items.values():
            total += (v["value"] * v["qty"])
        return total

if __name__ == "__main__":
    jeff = Cart('Jeff')
    jeff.add_to_cart('potato', 1.25, 3)
    print(jeff.sub_total())


