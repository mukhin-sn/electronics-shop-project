"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import *
# import pytest


# @pytest.fixture()
# def create_object():
#     return Item("Name", 1250, 2)


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
