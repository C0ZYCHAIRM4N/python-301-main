# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
import math


class Circle():
    """models a circle object"""
    def __init__ (self, radius):
        self.radius = radius

    def __area__ (self):
        return  

    def circumference(self):
        """calculates the circumference of a circle object"""
        return math.pi * self.radius ** 2

class Rectangle():
    """models a rectangle object"""
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of a rectangle object"""
        area = self.length * self.width
        print(area)


    def perimeter(self):
        

rectangle = Rectangle(3, 4)

rectangle.perimeter()