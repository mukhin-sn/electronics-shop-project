import pytest

from src.phone import *


def test_init_class():
    phone_1 = Phone("Nokia-6230i", 10500, 15, 1)
    assert phone_1.name == "Nokia-6230i"
    assert phone_1.price == 10500
    assert phone_1.quantity == 15
    assert phone_1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 0
    with pytest.raises(ValueError):
        phone_1.number_of_sim = -4
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 10.5
    with pytest.raises(TypeError):
        phone_1.name = 555


def test__repr__():
    phone_1 = Phone("Телефон", 100500, 40, 2)
    assert repr(phone_1) == "Phone('Телефон', 100500, 40, 2)"


def test_add():
    phone_1 = Phone("Sony-Z35", 100000, 27, 2)
    item_1 = Item("Кулер", 12000, 33)
    assert phone_1 + item_1 == 60
    with pytest.raises(ValueError):
        phone_1 + 25
