
from abc import abstractmethod, ABC
from math import sqrt

class Shape(ABC):

    def __init__(self):
        self._name = None
        self._color = 'Red'

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, name=None, color='Red'):
        super().__init__()

        self.__length = 0
        self.__breadth = 0
        self._name = name
        self._color = color

    """sets the dimension of the rectangle object """
    def set_dimension(self, length, breadth):
        self.__breadth = breadth
        self.__length = length


    """returns the area of the Reactangle object"""
    def get_area(self):
        return self.__length * self.__breadth

    """returns the perimeter of the rectangle object"""
    def get_perimeter(self):
        return 2 * (self.__breadth  +  self.__length)

class Triangle(Shape):

    def __init__(self, name=None, color='Red'):
        super().__init__()

        self.sideA = 3
        self.sideB = 4
        self.sideC = 5
        self._name = name
        self._color = color

    """using heron's formula to find the area"""
    def get_area(self):
        #semi perimeter
        s = (self.sideA + self.sideB + self.sideC) * 0.5
        return sqrt( s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC))

    """returns perimeter of the triangle"""
    def get_perimeter(self):
        return self.sideA + self.sideB + self.sideC



def main():

    rect = Rectangle("rec1", "blue")
    tri = Triangle("tri1", "yellow")
    rect.set_dimension(10, 20)

    #printing area and perimeter

    print("Area of Rectangle: ", rect.get_area())
    print("Area of Triangle: ", tri.get_area())

    print("Perimeter of Rectangle: ", rect.get_perimeter())
    print("Perimeter of triangle: ", tri.get_perimeter())


if __name__ == '__main__':
    main()

