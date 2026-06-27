from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityError
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ZeroQuantityError

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        super().__init__()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать разные типы товаров")

        return (self.price * self.quantity) + (other.price * other.quantity)
