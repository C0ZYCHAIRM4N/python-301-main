# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Magic:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def cast(self, target, caster):
        if caster.mana >= self.mana_cost:
            target.health -= self.damage
            caster.mana -= self.mana_cost
            print(f"{caster.name} casts {self.name} on {target.name} for {self.damage} damage! Mana left: {caster.mana}")
        else:
            print(f"{caster.name} doesn't have enough mana to cast {self.name}!")

    def __str__(self):
        return f"Magic(name={self.name}, damage={self.damage}, mana_cost={self.mana_cost})"

class FireMagic(Magic):
    def __init__(self, name, damage, mana_cost, burn_duration):
        super().__init__(name, damage, mana_cost)
        self.burn_duration = burn_duration

    def cast(self, target, caster):
        super().cast(target, caster)
        if caster.mana >= self.mana_cost:
            print(f"{target.name} is burned for {self.burn_duration} turns!")

    def __str__(self):
        return f"FireMagic(name={self.name}, damage={self.damage}, mana_cost={self.mana_cost}, burn_duration={self.burn_duration})"
        
class Firebolt(FireMagic):
        def __init__(self, name, damage, mana_cost, burn_duration, range):
            super().__init__(name, damage, mana_cost, burn_duration)
            self.range = range

        def cast(self, target, caster):
            if caster.mana >= self.mana_cost:
                if target.distance <= self.range:
                    super().cast(target, caster)
                    print(f"{target.name} is within range!")
                else:
                    print(f"{target.name} is out of range!")
            else:
                print(f"{caster.name} doesn't have enough mana to cast {self.name}!")

        def __str__(self):
            return f"Firebolt(name={self.name}, damage={self.damage}, mana_cost={self.mana_cost}, burn_duration={self.burn_duration}, range={self.range})"
    
class Melee:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def strike(self, target):
        if self.durability > 0:
            target.health -= self.damage
            self.durability -= 1
            print(f"{self.name} strikes {target.name} for {self.damage} damage! Durability left: {self.durability}")
        else:
            print(f"{self.name} is broken and can't be used anymore!")

    def __add__(self, other):
        if isinstance(other, Melee):
            new_name = f"{self.name} & {other.name}"
            new_damage = self.damage + other.damage
            new_durability = self.durability + other.durability
            return Melee(new_name, new_damage, new_durability)
        return NotImplemented

    def __str__(self):
        return f"Melee(name={self.name}, damage={self.damage}, durability={self.durability})"
    
class Sword(Melee):
    def __init__(self, name, damage, durability, sharpness):
        super().__init__(name, damage, durability)
        self.sharpness = sharpness

    def strike(self, target):
        if self.durability > 0:
            target.health -= self.damage * self.sharpness
            self.durability -= 1
            print(f"{self.name} strikes {target.name} for {self.damage * self.sharpness} damage! Durability left: {self.durability}")
        else:
            print(f"{self.name} is broken and can't be used anymore!")

    def __str__(self):
        return f"Sword(name={self.name}, damage={self.damage}, durability={self.durability}, sharpness={self.sharpness})"
        
        
        
        