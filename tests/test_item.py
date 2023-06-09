"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.item import InstantiateCSVError
from src.phone import Phone



@pytest.fixture()
def make_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def make_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_calculate_total_price(make_item):
    item1 = make_item
    assert item1.calculate_total_price() == 200000


def test_apply_discount(make_item):
    item1 = make_item
    Item.pay_rate = 0.8
    item1.apply_discount()
    expected = 8000
    assert item1.price == expected


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Smartphone'
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_csv('../tests/item.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../tests/items1.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../tests/items2.csv')


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_len_name():
    item1 = Item('Smartphone', 10000, 20)
    assert item1.name == 'Smartphone'
    with pytest.raises(Exception):
        item1.name = "Supersmartphone"


def test_repr(make_item):
    item1 = make_item
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(make_item):
    item1 = make_item
    assert str(item1) == 'Смартфон'


def test_addition(make_item, make_phone):
    item1 = make_item
    phone1 = make_phone
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        assert item1 + 10 == 40
        assert phone1 + 5 == 20


