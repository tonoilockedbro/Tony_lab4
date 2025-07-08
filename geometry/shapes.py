from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side_length: float):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)
