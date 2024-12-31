# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
import requests

# List of your six favorite Pokémon
favorite_pokemon = ["charmander", "ivysaur", "pikachu", "pidgeotto", "squirtle", "wartortle"]

# Base URL for the Pokémon API
base_url = "https://pokeapi.co/api/v2/pokemon/"

# Function to fetch Pokémon information
def fetch_pokemon_info(pokemon_name):
    response = requests.get(base_url + pokemon_name)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        number = data['id']
        types = [type_info['type']['name'] for type_info in data['types']]
        return {
            "name": name,
            "number": number,
            "types": types
        }
    else:
        return None

# Fetch and print information for each favorite Pokémon
for pokemon in favorite_pokemon:
    info = fetch_pokemon_info(pokemon)
    if info:
        print(f"Name: {info['name'].capitalize()}")
        print(f"Number: {info['number']}")
        print(f"Types: {', '.join(info['types']).capitalize()}")
        print("-" * 20)
    else:
        print(f"Failed to fetch information for {pokemon.capitalize()}")











