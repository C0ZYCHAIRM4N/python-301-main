# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Appliance():
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def __str__ (self):
        return f"{self.brand} ({self.type}) ({self.color})"

class Dog():
    def __init__(self, breed, size, gender, age):
        self.breed = breed
        self.size = size
        self.gender = gender
        self.age = age

    def __add__(self, other):
        """combines 2 dog breeds"""
        new_breed = self.breed + other.breed
        new_age = self.age + 1
        return Dog(breed = new_breed, age = new_age)


    def __str__ (self):
        return f"{self.breed} ({self.size}) ({self.gender}) ({self.age})"

class Meal():
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def __str__(self):
        return f"{self.breakfast} ({self.lunch}) ({self.dinner})"