# Funkcije


def add_number(param1, param2):
    return param1 + param2

# print(add_number())
# print(add_number(1))
# print(add_number(1,2))


def print_country(a=0, country = "Crna Gora"):
    if country == None: # rucno postavljanje default vrijednosti
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


print(ime_prezime(prezime="Boricic", ime="Boris"))

# Funkcija može da vrati više vrijednosti
def return_more_values(a,b,c):
    zbir = a + b + c
    proizvod = a * b * c
    return zbir, proizvod

zbir, proizvod = return_more_values(1, 2, 3)
print("Zbir je:" + zbir)
print("Proizvod je:" + proizvod)

# *args
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

# **kwargs
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")


