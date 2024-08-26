# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """_summary_
    """
    def __init__(self, name, diameter, distance_from_sun, moons):
        self.name = name
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.moons = moons
    pass
print(Planet("Earth", 12742, 93, 1))


