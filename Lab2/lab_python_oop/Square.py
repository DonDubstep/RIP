from Rectangle import Rect

class Square(Rect):
    name = "Квадрат"

    def __init__(self, side, colour):
        if not isinstance(side, str):
            self.width = side
            self.height = side
            self.thisColour.colour = colour
        else:
            print("Значение стороны введено неверно")

    def Area(self):
        return super().Area()

    def repr(self):
        try:
            print("{} цвета {} длиной {} имеет площадь {}".format(self.name, self.thisColour.colour, self.width, self.Area()))
        except:
            print("Ошибка: неверно указаны параметры квадрата")