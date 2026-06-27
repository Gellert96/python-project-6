from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Category(BaseEntity):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        super().__init__(name, description)
        self.__products = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product):
        try:
            if not isinstance(product, Product):
                raise TypeError

            if product.quantity == 0:
                raise ZeroQuantityError

            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")

        except ZeroQuantityError as error:
            print(error)
            raise

        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        return [str(p) for p in self.__products]

    def middle_price(self):
        try:
            return sum(p.price for p in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
