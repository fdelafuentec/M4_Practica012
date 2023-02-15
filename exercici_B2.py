import json

#amb aquesta funcio llegim el arxiu creat abans.
def llegirArxiu():
    with open("bookstore", "r") as file:
        result = json.load(file)
        print(result)
