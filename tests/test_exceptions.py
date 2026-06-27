import pytest

from src.category import Category
from src.exceptions import ZeroQuantityError
from src.product import Product


def test_product_zero_quantity_error():
    with pytest.raises(ZeroQuantityError):
        Product("Bad product", "Zero quantity", 1000, 0)


def test_category_middle_price():
    product1 = Product("Product 1", "Desc", 100, 5)
    product2 = Product("Product 2", "Desc", 200, 10)

    category = Category("Test", "Test category", [product1, product2])

    assert category.middle_price() == 150


def test_category_middle_price_empty():
    category = Category("Empty", "Empty category", [])

    assert category.middle_price() == 0


def test_add_product_zero_quantity_error():
    category = Category("Test", "Test category", [])
    product = Product("Product", "Desc", 100, 1)
    product.quantity = 0

    with pytest.raises(ZeroQuantityError):
        category.add_product(product)
