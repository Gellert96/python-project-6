from src.product import Product
from src.category import Category


def test_product_str():
    p = Product("Apple", "desc", 100, 5)
    assert str(p) == "Apple, 100 руб. Остаток: 5 шт."


def test_category_str():
    p = Product("Apple", "desc", 100, 5)
    c = Category("Fruits", "desc", [p])

    assert str(c) == "Fruits, количество продуктов: 5 шт."


def test_product_add():
    p1 = Product("Apple", "desc", 100, 10)
    p2 = Product("Banana", "desc", 200, 2)

    assert p1 + p2 == 1400