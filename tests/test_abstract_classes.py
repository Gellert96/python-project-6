from src.order import Order
from src.product import Product


def test_order_init():
    product = Product(
        "Apple",
        "Fresh apple",
        100,
        5,
    )

    order = Order(product, 3)

    assert order.product == product
    assert order.quantity == 3
    assert order.total_price == 300


def test_order_str():
    product = Product(
        "Apple",
        "Fresh apple",
        100,
        5,
    )

    order = Order(product, 2)

    assert (
        str(order)
        == "Заказ: Apple, количество: 2 шт., итоговая стоимость: 200 руб."
    )


def test_order_type_error():
    import pytest

    with pytest.raises(TypeError):
        Order("Not product", 1)
