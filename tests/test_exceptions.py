import pytest

from src.category import Category
from src.exceptions import ZeroQuantityError
from src.product import Product


def test_product_zero_quantity_error():
    with pytest.raises(
        ZeroQuantityError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_zero_quantity_error_is_value_error():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_category_middle_price():
    product1 = Product("Product 1", "Desc", 100, 5)
    product2 = Product("Product 2", "Desc", 200, 10)
    product3 = Product("Product 3", "Desc", 300, 15)

    category = Category("Test", "Test category", [product1, product2, product3])

    assert category.middle_price() == 200


def test_category_middle_price_empty():
    category = Category("Empty", "Empty category", [])

    assert category.middle_price() == 0


def test_add_product_success_message(capsys):
    category = Category("Test", "Test category", [])
    product = Product("Product", "Desc", 100, 1)

    category.add_product(product)

    captured = capsys.readouterr()

    assert "Товар добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_product_zero_quantity_error(capsys):
    category = Category("Test", "Test category", [])
    product = Product("Product", "Desc", 100, 1)
    product.quantity = 0

    with pytest.raises(ZeroQuantityError):
        category.add_product(product)

    captured = capsys.readouterr()

    assert "Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out