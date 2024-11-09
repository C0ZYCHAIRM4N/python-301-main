# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """_blueprint for a planet
    """
    def __init__(self, name, diameter, distance_from_sun, moons):
        self.name = name
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    def __str__ (self):
        return f"{self.name} {self.diameter} {self.distance_from_sun} {self.moons}"
    
planet = Planet("mars", 1000, 1234, 3)

print(planet)
    
    


