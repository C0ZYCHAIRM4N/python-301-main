# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

# request json response from the API

# import requests module to access the API
import requests
import json


response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
# convert the response from JSON to a list of dictionaries and save that list under the variable name data
data = response.json()

# Create new file called ghibli_cats.json and serialize the data back into json data to save in file
# with the help of the json module.

with open("ghibli_cats.json", "w") as fout:
    json.dump(data, fout)

# 


