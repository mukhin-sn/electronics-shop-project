"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import *

# import pytest


# @pytest.fixture()
# def create_object():
#     return Item("Name", 1250, 2)


def test_item_name():
    item = Item("Телефон", 10000, 5)
    assert item.name == "Телефон"
    item.name = 3 * "Bla"
    assert item.name == "BlaBlaBla"
    item.name = "Very" + 3 * "Bla"
    assert item.name == "VeryBlaBla"


def test_item_calculate_total_price():
    item_0 = Item("Name", 1250, 2)
    assert item_0.name == "Name"
    assert item_0.price == 1250
    assert item_0.quantity == 2


def test_apply_discount():
    item_1 = Item("Name", 1000, 3)
    Item.pay_rate = 0.5
    item_1.apply_discount()
    assert item_1.price == 500


def test_instantiate_from_csv():
    Item.instantiate_from_csv("../src/items.csv")
    # assert len(Item.all) == 5
    item_3 = Item.all[2]
    assert item_3.name == "Кабель"
    assert item_3.price == "10"
    assert item_3.quantity == "5"


def test_string_to_number():
    assert Item.string_to_number("12") == 12
    assert Item.string_to_number("10.0") == 10
    assert Item.string_to_number("125.3") == 125
