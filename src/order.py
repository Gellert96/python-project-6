from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        try:
            if not isinstance(product, Product):
                raise TypeError

            if product.quantity == 0 or quantity == 0:
                raise ZeroQuantityError

            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity

            super().__init__(product.name, product.description)

            print("Товар добавлен")

        except ZeroQuantityError as error:
            print(error)
            raise

        finally:
            print("Обработка добавления товара завершена")

    def __str__(self):
        return (
            f"Заказ: {self.name}, "
            f"количество: {self.quantity} шт., "
            f"итоговая стоимость: {self.total_price} руб."
        )
