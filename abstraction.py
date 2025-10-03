from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Class
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Usage
rect = Rectangle(10, 5)
print("Area:", rect.area())  # Output: Area: 50
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 30
