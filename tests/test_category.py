from src.category import Category
from src.product import Product


def test_category_init():
    product = Product("Apple", "Fresh apple", 100.5, 10)
    category = Category("Fruits", "All fruits", [product])

    assert category.name == "Fruits"
    assert category.description == "All fruits"
    assert len(category.products) == 1


def test_category_count():
    Category.category_count = 0

    product = Product("Apple", "desc", 100, 2)

    Category("Fruits", "desc", [product])
    Category("Veggies", "desc", [])

    assert Category.category_count == 2


def test_add_product():
        Category.product_count = 0

        category = Category("Fruits", "desc", [])

        product = Product("Apple", "Fresh apple", 100, 5)

        category.add_product(product)

        assert len(category.products) == 1
        assert Category.product_count == 1


def test_products_property():
    product = Product("Apple", "Fresh apple", 100, 5)

    category = Category("Fruits", "desc", [product])

    expected = ["Apple, 100 руб. Остаток: 5 шт."]

    assert category.products == expected
