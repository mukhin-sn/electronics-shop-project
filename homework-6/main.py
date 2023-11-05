from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('items.csv')
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле item.csv удалена последняя колонка.
    Item.instantiate_from_csv('../src/item.csv')
    # InstantiateCSVError: Файл item.csv поврежден
