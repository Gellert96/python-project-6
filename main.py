from src.product import Product
from src.category import Category
from src.json_loader import load_data


if __name__ == "__main__":
    categories = load_data("products.json")

    for category in categories:
        print(category.name)
        print(category.description)
        print(len(category.products))

    print(Category.category_count)
    print(Category.product_count)
