"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import csv


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

def test_instantiate_from_csv():
    Item.all = []
    with open("../tests/items.csv", newline="") as file:
        reader = csv.DictReader(file)
        for line in reader:
            Item.all.append(line)
    assert Item.all[0] == {'name': 'Smartphone', 'price': '100', 'quantity': '1'}
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


