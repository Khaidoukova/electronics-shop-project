from src.item import Item


class LanguageMixin:
    def __init__(self):
        self.__language = "EN"
    def change_lang(self):
        if self.language == "RU":
            self.language = "EN"
        elif self.language == "EN":
            self.language = "RU"



class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def






#kb = Keyboard('Dark Project KD87A', 9600, 5)
#print(kb)
#kb.change_lang()
#print(kb.language)

