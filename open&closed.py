from abc import ABC, abstractmethod


#violating open closed principle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    
 #achieving open closed principle
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def calculate_area(shapes):
    for shape in shapes:
        print(f'The area is: {shape.area()}')

shapes = [Rectangle(10, 20), Circle(5)]
calculate_area(shapes)
