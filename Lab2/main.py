import sys
sys.path[0] += r"\\lab_python_oop"
from Rectangle import Rect
from Square import Square
from Circle import Circle
from PIL import Image

def main():
    N = 8
    rect = Rect(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")
    rect.repr()
    circle.repr()
    square.repr()

    im = Image.open("D:\\ProgRAMS\\Python\\lab_python_oop\\qwerty.png")
    im.show()

if __name__ == "__main__":
    main()