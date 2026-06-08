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


def test_new_product():
    data = {
        "name": "Samsung",
        "description": "Phone",
        "price": 1000,
        "quantity": 5,
    }

    product = Product.new_product(data)

    assert product.name == "Samsung"
    assert product.description == "Phone"
    assert product.price == 1000
    assert product.quantity == 5


def test_price_setter_positive():
    product = Product("Apple", "Fresh apple", 100, 5)

    product.price = 200

    assert product.price == 200


def test_price_setter_negative():
    product = Product("Apple", "Fresh apple", 100, 5)

    product.price = -10

    assert product.price == 100
