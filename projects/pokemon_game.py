# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = max_hp

    def battle(self, opponent):
        if self.primary_type == "water" and opponent.primary_type == "fire":
            print(f"{self.name} wins!")
        elif self.primary_type == "fire" and opponent.primary_type == "grass":
            print(f"{self.name} wins!")
        elif self.primary_type == "grass" and opponent.primary_type == "water":
            print(f"{self.name} wins!")
        else:
            print(f"{opponent.name} wins!")
            self.hp -= 10

    def feed(self):
        self.hp += 10
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} has been fed and now has {self.hp} hp.")

# Instantiate Pokemon objects
charmander = Pokemon("Charmander", "fire", 50)
squirtle = Pokemon("Squirtle", "water", 50)
bulbasaur = Pokemon("Bulbasaur", "grass", 50)

charmander.battle(squirtle)








