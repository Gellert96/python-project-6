from src.product import Product
from src.category import Category


def test_product_init():
    product = Product("Apple", "Fresh apple", 100.5, 10)

    assert product.name == "Apple"
    assert product.description == "Fresh apple"
    assert product.price == 100.5
    assert product.quantity == 10


def test_product_count():
    Category.product_count = 0

    p1 = Product("Apple", "desc", 100, 2)
    p2 = Product("Banana", "desc", 50, 5)

    Category("Fruits", "desc", [p1, p2])

    assert Category.product_count == 2