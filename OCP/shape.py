from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class ShapeAreaCalculator:
    def area(self, shape):
        return shape.area()


rec_area = Rectangle(23, 46)
print(rec_area)

shape_ar = ShapeAreaCalculator()
print(shape_ar.area(rec_area))

rec_circle = Circle(14)
print(rec_circle)

print(shape_ar.area(rec_circle))