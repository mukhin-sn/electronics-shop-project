from src.item import *


class MixinKeyboard:
    LN = "EN"

    def __init__(self):
        self.lang = self.LN

    def change_lang(self):
        if self.lang == "EN":
            self.lang = "RU"


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language
