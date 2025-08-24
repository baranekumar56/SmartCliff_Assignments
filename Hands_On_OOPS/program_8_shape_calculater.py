
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def calculate_area(self):
        return self.__length * self.__breadth

    def calculate_perimeter(self):
        return 2 * (self.__breadth + self.__length)

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * (self.__radius * self.__radius)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

def main():

    rec = Rectangle(5, 3)
    cir = Circle(5)

    print("Area of Rectangle :", rec.calculate_area())
    print("Area of Circle: ", cir.calculate_area())

    print("Perimeter of Rectangle: ",rec.calculate_perimeter())
    print("Perimeter of Circle: ", cir.calculate_perimeter())

if __name__ == "__main__":
    main()