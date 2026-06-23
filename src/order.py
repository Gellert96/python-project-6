from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

        super().__init__(product.name, product.description)

    def __str__(self):
        return (
            f"Заказ: {self.name}, "
            f"количество: {self.quantity} шт., "
            f"итоговая стоимость: {self.total_price} руб."
        )
