import json
#creem el json
bookstore = """
    {
    "book": [
        {"title":"El señor de los anillos",
         "cover":"verda",
         "year":"1998",
         "pages":"674"
        }
        {"title":"La historia interminable",
         "cover":"blanca",
         "year":"1992",
         "pages":"497"
        }
        {"title":"Damian",
         "cover":"negra",
         "year":"2022",
         "pages":"197"
        }
        {"title":"La vecina rubia",
         "cover":"groga",
         "year":"2021",
         "pages":"248"
        }
"""

#aquí agafem el bookstore i indiquem que volem escriure un nou arxiu ("w") amb el nom "bookstore".
with open("bookstore", "w") as file:
    json.dump(bookstore,file)

print(bookstore)