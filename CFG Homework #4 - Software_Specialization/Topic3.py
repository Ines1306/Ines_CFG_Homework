import abc
from math import sqrt


class Shape(object):
    @abc.abstractmethod
    def calc_perimeter(self, input):
        return

    @abc.abstractmethod
    def calc_area(self, input):
        return

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def calc_perimeter(self):
        perim = self.a * 4
        return perim

    def calc_area(self):
        area = self.a * 2
        return area

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = self.a * 2 + self.b * 2
        return perim

    def calc_area(self):
        area = self.a * self.b
        return area

class RightAngledTriangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calc_perimeter(self):
        perim = self.height + self.base + int(sqrt(self.height**2+self.base**2))
        return perim

    def calc_area(self):
        area = int(self.height * self.base * 1/2)
        return area

s = Square(6)
print(s.calc_perimeter())
# should get 24
print(s.calc_area())
# should get 12
r = Rectangle(6, 4)
print(r.calc_perimeter())
# should get 20
print(r.calc_area())
# should get 24
t = RightAngledTriangle(9,12)
print(t.calc_perimeter())
# should get 36
print(t.calc_area())
# should get 54