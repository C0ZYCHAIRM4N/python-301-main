# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.
import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

def find_recipes_with_ingredient(ingredient):
    links = soup.find_all("a")
    matching_recipes = []
    
    for link in links:
        if ingredient.lower() in link.text.lower():
            matching_recipes.append(link)
    
    return matching_recipes

# Ask for ingredient
ingredient = input("Enter an ingredient: ").strip().lower()

# Find recipes containing the ingredient
matching_recipes = find_recipes_with_ingredient(ingredient)

# Print recipes that contain the ingredient
if matching_recipes:
    print(f"Recipes containing '{ingredient}':")
    for recipe in matching_recipes:
        print(f"- {recipe.text}")
        print(f"  Link: {recipe['href']}\n")
else:
    print(f"No recipes found containing '{ingredient}'.")






