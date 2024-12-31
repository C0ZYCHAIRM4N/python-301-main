# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import requests

# Base URL for the Ghibli API
base_url = "https://ghibliapi.herokuapp.com"

# Function to fetch data from a given endpoint
def fetch_data(endpoint):
    response = requests.get(f"{base_url}/{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Fetch species data to find the cat species
species_data = fetch_data("species")
cat_species = None
for species in species_data:
    if "cat" in species['name'].lower():
        cat_species = species
        break

if cat_species:
    print(f"Cat Species: {cat_species['name']}")
    print(f"Description: {cat_species['description']}")
    print("-" * 40)

    # Fetch people data to find characters belonging to the cat species
    people_data = fetch_data("people")
    cat_characters = [person for person in people_data if person['species'] == cat_species['url']]

    # Display information about cat characters
    for character in cat_characters:
        print(f"Name: {character['name']}")
        print(f"Gender: {character['gender']}")
        print(f"Age: {character['age']}")
        print(f"Films: {', '.join(character['films'])}")
        print("-" * 40)
else:
    print("No cat species found in the Ghibli API.")


