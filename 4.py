class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = 5

    def set_quant(self, price):
        if (0 < price <100):
            self.__price = price
        else:
            print('Недопустимое значение!')

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class ItemDiscountReport(ItemDiscount):

    def __init__(self, __name, __price):
        super().__init__(__name, __price)

    def get_parent_data(self):
        return print(f"название {self.name} цена  {self.price}")

a = ItemDiscount('as', 7)
print(f' название {a.get_name()} цена {a.get_price()}')

a.set_quant(20)
print(f' название {a.get_name()} цена {a.get_price()}')

b = ItemDiscountReport('new',3)

b.set_quant(120)
print(f" Название: {b.get_name()} цена: {b.get_price()}")

b.set_quant(20)
print(f" Название: {b.get_name()} цена: {b.get_price()}")
