# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
import math


class Circle():
    def __init__ (self, radius):
        self.radius = radius

    def circumference(self):
        return math.pi * self.radius ** 2


    
        
class Rectangle():
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

rectangle = Rectangle(3, 4)

rectangle.perimeter()