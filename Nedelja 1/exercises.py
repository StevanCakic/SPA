# Prvi dio
# Varijable

# Zadatak 1
# Kreirati sledeće varijable:
    # ime koja sadrži vaše ime
    # prezime koja sadrži vaše prezime
    # godine koja sadrži vaše godine
    # email koja sadrži vašu email adresu
# Štampati rezultat u sledećem formatu:
    # Email adresa korisnika {ime} {prezime} ({godine}) je {email}.

ime = "Stevan"
prezime = "Cakic"
godine = 26
email = "stevan.cakic@udg.edu.me"

print(f"Email adresa korisnika {ime} {prezime} ({godine}) je {email}")

# Drugi dio
# Brojevi

# Isprobajte aritmetičke operacije sa integer i floating brojevima.
    # Sta je rezultat operacije 0.1 + 0.2?
    # Isporbati operator **
        # Kako da nađete korijen broja koristeći ** operator?
    # Isprobati operator eksponent (e)
        # Šta je rezultat 4e2

# Treci dio
# Casting
# Isprobati par konverzija iz jednog tipa podatka u drugi

# Zadatak 2
# Ako je cijena računara 400e, štampati koliko treba odvojite za plaćanje PDVa
# Štampati rezultat u sledećem formatu:
    # Cijena računara je 400e. Iznos PDVa je {pdv}, a cijena računara bez PDVa je {cijena bez PDVa}

cijena = 400
pdv = 0.21 * cijena

print(f"Cijena racunara je {cijena}e. Iznos PDVa je {pdv}, a cijena racunara bez PDVa je {cijena - pdv}")

# Četvri dio
# Stringovi

# Testirati len(str), str[index]
# upper(), split(), capitalize()

# Zadatak 3
# Iz unijetog stringa izvuci svaki treci karakter za prvih 10 karaktera stringa
string = "Imamo neki proizvoljan string"
print(string[0:10:3])

# Zadatak 4

'''
Napisati program koji vraća broj malih i broj velikih slova za zadati string.
Primjer: upper_lower(“Hi Mr. Rober. How are you today?”), vraća (19, 4), 19 - broj malih slova, 4 - broj velikih slova. Pomoć: da provjeriti da li je karakter slovo koristiti isalpha metod.
'''


def upper_lower(string):
    num_lower = 0
    num_upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                num_lower += 1
            else:
                num_upper += 1

    return num_lower, num_upper


print(upper_lower("AbabaaC 11"))

# Zadatak 5
# Korisnik unosi tri broja.
# Naći minimum i maksimum među unijetim brojevima i rezultat prikazati korisniku


def minimum(num1, num2, num3):
    _min = num1
    if num2 <= _min:
        _min = num2
    if num3 <= _min:
        _min = num3
    return _min


def maximum(num1, num2, num3):
    _max = num1
    if num2 >= _max:
        _max = num2
    if num3 >= _max:
        _max = num3
    return _max


def min_max(num1, num2, num3):
    _min = minimum(num1, num2,num3)
    _max = maximum(num1, num2, num3)
    return _min, _max


print(min_max(10, -10, 3))


# Zadatak 6
# Napisati program koji racuna zbir parnih i proizvod neparnih brojeva od 1 do 15
# Takodje, prikazati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta

def even_odd():
    num_even = 0
    num_odd = 0
    suma = 0
    product = 1
    for num in range(1,16):
        if num % 2 == 0:
            num_even += 1
            suma += num
        else:
            num_odd += 1
            product *= num

    print(f"Number of even numbers: {num_even} and sum is {suma}, number of odd numbers:{num_odd} and product is {product}.")

even_odd()