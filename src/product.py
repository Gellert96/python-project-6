class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, data: dict, products_list=None):
        if products_list is None:
            return cls(
                data["name"],
                data["description"],
                data["price"],
                data["quantity"],
            )

        for product in products_list:
            if product.name == data["name"]:
                product.quantity += data["quantity"]

                if data["price"] > product.price:
                    product.price = data["price"]

                return product

        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"],
        )
