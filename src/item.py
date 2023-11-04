import csv
from src.instantiate_csv_error import *


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not issubclass(other.__class__, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них.")
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name='../src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open(file_name) as data_file:
                read_file = csv.DictReader(data_file)
                fieldnames = read_file.fieldnames
                for file in read_file:
                    name = file[fieldnames[0]]
                    price = file[fieldnames[1]]
                    quantity = file[fieldnames[2]]
                    cls(name, price, quantity)
        except FileNotFoundError:
            print(f"Отсутствует файл {file_name}")
        else:
            print("OK")

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))
