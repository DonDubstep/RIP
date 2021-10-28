from Shape import Shape
from Colour import Colour

class Rect(Shape):

    thisColour = Colour()
    name = "Прямоугольник"

    def __init__(self, width, height, colour):
        if not isinstance(width, str) and not isinstance(height, str):
            self.width = width
            self.height = height
            self.thisColour.colour = colour
        else:
            print("Ошибка: неверно указаны параметры прямоугольника")

    def Area(self):
        return self.width * self.height

    def repr(self):
        try:
            print("{} цвета {} длиной {} высотой {} имеет площадь {}".format(self.name, self.thisColour.colour, self.width, self.height, self.Area()))
        except:
            print("Ошибка: неверно указаны параметры прямоугольника")