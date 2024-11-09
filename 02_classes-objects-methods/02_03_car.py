# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    """Creates an empty car object"""
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
    
    def increase_speed(self):
        """increase max speed by 5"""
        self.max_speed += 5
        print(f"{self.max_speed}")
        
    
    def details_of_car(self):
        """prints details of car"""
        print(f"{self.model} {self.year} {self.max_speed}")


car = Car("honda", 1990, 80)
car.increase_speed()

car = Car("chevy", 2016, 100)





        
