from src.lawn_grass import LawnGrass
from src.product import Product


def test_lawn_grass_init():
    grass = LawnGrass(
        "Газон",
        "Зеленая трава",
        500,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert grass.name == "Газон"
    assert grass.description == "Зеленая трава"
    assert grass.price == 500
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_lawn_grass_is_product():
    grass = LawnGrass(
        "Газон",
        "Зеленая трава",
        500,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert isinstance(grass, Product)
