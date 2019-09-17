# Funkcije

def add_number(param1, param2):
    return param1 + param2

# print(add_number())
# print(add_number(1))
# print(add_number(1,2))

def print_country(a="", country = "Crna Gora"):
    if country == None:
        country = "Crna Gora"

    print("Ja sam iz " + country)

print_country(country="Drzava", a=10)

def print_food(food):
  for x in food:
    print(x)

# print_country("Italija")
# fruits = ["apple", "banana", "cherry"]
# print_food(fruits)

def ime_prezime(ime="Marko", prezime="Markovic"):
    return f'{ime} {prezime}'

print("")
print(ime_prezime(prezime="Prezime", ime="Ime"))
