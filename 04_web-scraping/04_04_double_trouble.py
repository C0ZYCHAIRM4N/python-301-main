# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.


import requests

# API endpoints
api1 = "https://api.coingecko.com/api/v3/coins/bitcoin"
api2 = "https://api.coingecko.com/api/v3/coins/ethereum"

# Make calls to both APIs
response1 = requests.get(api1)
response2 = requests.get(api2)

# Extract relevant data from both responses
data1 = response1.json()
data2 = response2.json()

# Combine the data from both APIs
combined_data = {
    "bitcoin": {
        "name": data1["name"],
        "current_price": data1["market_data"]["current_price"]["usd"],
        "market_cap": data1["market_data"]["market_cap"]["usd"]
    },
    "ethereum": {
        "name": data2["name"],
        "current_price": data2["market_data"]["current_price"]["usd"],
        "market_cap": data2["market_data"]["market_cap"]["usd"]
    }
}

# Print the combined data
print(combined_data)






