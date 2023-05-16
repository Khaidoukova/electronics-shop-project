"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    expected = 200000
    assert item1.calculate_total_price() == expected

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    expected = 8000
    assert item1.price == expected
