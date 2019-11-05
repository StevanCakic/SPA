# Napisati funkciju koja stampa da li je uneseni broj pozitivan (0 poz) ili ne
def is_positive(a):
    if a >= 0:
        print("Pozitivan")
    else:
        print("Negativan")

def is_positive_v2(a):
    if a >= 0:
        return True
    else:
        return False

def is_positive_v3(a):
    return a >= 0

#is_positive(-5)
#print(is_positive_v2(-5))
#print(is_positive_v3(-5))

# Provjeravamo da li se broj c nalazi izmedju a i b (ukljucujuci)
def ran_inclusive(a, b, c):
    return c >= a and c <= b

# print(ran_inclusive(5, 10, 11))

def compute_sum_and_product(n):
    suma = 0
    proizvod = 1
    for i in range(1, n+1):
        suma = suma + i
        proizvod = proizvod * i

    return suma, proizvod

s, p = compute_sum_and_product(4)
#print(s)
#print(p)

# Naci sumu elemenata liste do prvog negativnog broja
def sum_upto_negative(lista):
    suma = 0
    for element in lista:
        if element >= 0:
            suma = suma + element
        else:
            break
    return suma

# print(sum_upto_negative([1,2,3,7,-1,2,3]))

# Napisati fun. koja racuna sumu kvadrata parnih brojeva prvih n prirodnih brojeva
def sum_square_of_even_nums(n):
    suma = 0
    for number in range(1, n+1):
        if number % 2 == 0:
            suma = suma + number ** 2
    return suma

# n = int(input("Unesite prirodan broj n:"))
# print(f"Rezultat sume je:{sum_square_of_even_nums(n)}")

def suma_squared(a, b):
    s = 0
    for i in range(a, b+1):
        s = s + i**2
    return s

#a = int(input("Unesite pocetak segmenta:"))
#b = int(input("Unesite kraj segmenta:"))

#print(f"Suma kvadrata u zadatom segmentu je: {suma_squared(a, b)}")
def find_index(lista, number):
    for index, element in enumerate(lista):
        if element >= number:
            return index

'''
a = ["a", "b", "c", "d"]
for index, value in enumerate(a):
    print("index:", index)
    print("value:", value)
'''

def get_digits(string):
    number = ""
    for char in string:
        if char.isdigit():
            number = number + char
    
    return int(number)

# string = input("Unesite neki string:")
# print(get_digits(string))

def upper_lower(string):
    num_of_lower = 0
    num_of_upper = 0
    for char in string:
        if char.islower():
            num_of_lower += 1
        if char.isupper():
            num_of_upper += 1
    
    return num_of_lower, num_of_upper

#string = input("Unesite neki string:")
#num_of_lower, num_of_upper = upper_lower(string)
#print(num_of_lower, num_of_upper)

def short_string(string, limit):
    return string[0:limit] + "..."

print(short_string("Neki string", 4))