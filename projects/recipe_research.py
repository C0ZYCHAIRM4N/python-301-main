# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.
class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."

    def search_url(self):
        """Creates a URL to search for recipes using this ingredient."""
        base_url = "https://www.google.com/search?q="
        query = f"recipes with {self.name}"
        return base_url + query.replace(" ", "+")

class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")
    
    def expire(self):
        print(f"your {self.name} has expired. it's probably still good.")
        self.name = "old " + self.name

# Prompt the user for input
ingredient_name = input("Enter the name of the ingredient: ")
ingredient_amount = input("Enter the amount of the ingredient: ")

# Create an instance of Ingredient with the user input
ingredient = Ingredient(ingredient_name, ingredient_amount)

# Print the search URL for recipes using the inputted ingredient
print(ingredient.search_url())