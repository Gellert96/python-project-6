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