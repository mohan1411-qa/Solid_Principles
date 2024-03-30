class ShapeAreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return 3.14159 * shape.radius**2
        if isinstance(shape, Rectangle):
            return shape.width * shape.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

