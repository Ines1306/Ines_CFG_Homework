import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

# Creating subclass Rectangle
class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = (self.a + self.b) * 2
        print("Consider me implemented", perim)
        return perim

# Creating subclass Square
class Square(Rectangle):

    def __init__(self, a):
        Rectangle.__init__(self, a, a)
        # to make sure that a and b from Rectangle are equal to a from Square


# Creating an instance for each class
triangle_a = Triangle(1,2,3)
triangle_b = Triangle(4,5,6)
rectangle_a = Rectangle(1,2)
rectangle_b = Rectangle(3,4)
square_a = Square(1)
square_b = Square(2)

shapes = [triangle_a, triangle_b, rectangle_a, rectangle_b, square_a, square_b]

# Printing out the result of the calc_perimeter method
for shape in shapes:
    print(f"The perimeter of this {shape.__class__.__name__.lower()} is {shape.calc_perimeter()}")
    print('-'*10)
