from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def parameter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__()
        self.__radius = radius
    
    def parameter(self) -> float:
        return 2 * (pi*self.__radius)

    def area(self) -> float:
        return pi * (self.__radius**2)

class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        super().__init__()
        self.__length = length
        self.__width = width
    
    def parameter(self) -> float:
        return 2 * (self.__length + self.__width)

    def area(self) -> float:
        return self.__length * self.__width
    
circle = Circle(5)
rect = Rectangle(5, 3)
print(circle.area(), circle.parameter())
print(rect.area(), rect.parameter())
