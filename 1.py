class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return print(f"название {self.name} цена  {self.price}")

a = ItemDiscountReport('as', 7)
a.get_parent_data()