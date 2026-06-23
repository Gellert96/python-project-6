import json
from src.json_loader import load_data
from src.category import Category


def test_load_data(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "Test",
                    "price": 180000,
                    "quantity": 5,
                }
            ],
        }
    ]

    file_path = tmp_path / "products.json"
    file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_data(str(file_path))

    # проверяем, что вернулся список категорий
    assert isinstance(categories, list)
    assert len(categories) > 0

    category = categories[0]

    # проверяем категорию
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"

    # проверяем продукты (У ТЕБЯ ЭТО СТРОКИ)
    assert isinstance(category.products, list)
    assert len(category.products) > 0

    assert isinstance(category.products[0], str)
    assert "Samsung" in category.products[0]
