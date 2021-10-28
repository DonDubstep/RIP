class Colour:

    def __init__(self, colour):
        self.__colour = colour

    def __init__(self):
        pass

    @property
    def colour(self):
        return self.__colour
    
    @colour.setter
    def colour(self, colour):
        if isinstance(colour, str):
            self.__colour = colour
        else:
            print("Неверно введён цвет")

