class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class ItemDiscountReport(ItemDiscount):
    def __init__(self, __name, __price):
        super().__init__(__name, __price)

    def get_parent_data(self):
        return print(f"название {self.__name} цена  {self.__price}")


a = ItemDiscountReport('as', 7)
a.get_parent_data()

#