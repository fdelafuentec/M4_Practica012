import json

with open ("bookstore", "r") as file:
    result = json.load(file)
    print(result)