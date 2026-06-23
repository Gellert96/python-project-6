from src.smartphone import Smartphone


def test_smartphone_init():
    phone = Smartphone(
        "iPhone",
        "Телефон",
        100000,
        5,
        95.5,
        "15 Pro",
        256,
        "Black",
    )

    assert phone.name == "iPhone"
    assert phone.description == "Телефон"
    assert phone.price == 100000
    assert phone.quantity == 5
    assert phone.efficiency == 95.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"
