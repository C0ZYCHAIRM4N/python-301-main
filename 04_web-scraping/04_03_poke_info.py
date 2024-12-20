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
from bs4 import BeautifulSoup

# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
URL = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
six_pokemon = soup.find_all('a', href=True)
print(six_pokemon)











