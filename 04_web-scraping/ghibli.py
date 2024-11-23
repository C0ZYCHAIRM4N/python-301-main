import json

with open("ghibli_cats.json", "r") as fin:
    data = json.load(fin)

print(len(data))  # OUTPUT: 21
print(type(data))  # OUTPUT: <class 'list'>
