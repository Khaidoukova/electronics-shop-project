import csv
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        try:
            if len(new_name) <= 10:
                self.__name = new_name
        except:
            raise AttributeError("Длина названия больше 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализируем экземпляры класса данными из файла"""
        cls.all.clear()
        with open('../src/items.csv', newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                cls(line["name"], line["price"], line["quantity"])


    @staticmethod
    def string_to_number(line):
        numb = int(float(line))
        return numb

    def calculate_total_price(self):

        return self.price * self.quantity

    def apply_discount(self):

        self.price *= self.pay_rate
