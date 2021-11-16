class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport1(ItemDiscount):

    def __init__(self, name, price):
        super().__init__(name, price)

    def get_info(self):
        return print(f'название 1: {self.name}')


class ItemDiscountReport2(ItemDiscount):

    def __init__(self, name, price):
        super().__init__(name, price)

    def get_info(self):
        return print(f' цена 2: {self.price}')


a = ItemDiscountReport1('a', 10)
a.get_info()

b = ItemDiscountReport2('b', 20)
b.get_info()

for obj in (a, b):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(a)
obj_handler(b)
