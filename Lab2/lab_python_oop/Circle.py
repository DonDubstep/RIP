from math import pi
from Shape import Shape
from Colour import Colour

class Circle(Shape):
    thisColour = Colour()
    name = "Круг"

    def __init__(self, radius, colour):
        if not isinstance(radius, str):
            self.radius = radius
            self.thisColour.colour = colour
        else:
            print("Неверный формат данных")

    def Area(self):
        return self.radius * self.radius * pi
    
    def repr(self):
        try:
            print("{} цвета {} радиусом {}".format(self.name, self.thisColour.colour, self.radius))
        except:
            print("Ошибка: неверно указаны параметры круга")