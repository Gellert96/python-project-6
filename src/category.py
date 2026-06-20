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

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [str(p) for p in self.__products]

    def __str__(self):
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
