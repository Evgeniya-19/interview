class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, sale):
        super().__init__(name, price)
        self.sale = sale

    def get_parent_data(self):
        return print(f"название {self.name} цена  {self.price}")

    def __str__(self):
        new_price = self.price-self.price*self.sale/100
        return f" Цена со скидкой = {new_price}"

a = ItemDiscountReport('as', 100, 20)
print(a.__str__())


