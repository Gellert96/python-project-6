from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        ]
