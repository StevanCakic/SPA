def doors(n):
    lista = []
    for i in range(n):
        lista.append(0)
    for student in range(1, n+1):
        for pozicija, stanje in enumerate(lista):
            if (pozicija + 1) % student == 0:
                if stanje == 0:
                    lista[pozicija] = 1
                else:
                    lista[pozicija] = 0

    suma = 0
    for i in lista:
        suma += i

    return suma

print(doors(10))

def get_digits(str):
    lista = []
    for char in str:
        if char.isdigit():
            lista.append(char)
    
    spojena = "".join(lista)
    return int(spojena)

print(type(get_digits("1212 hdadah12")))

def check_password(input_string, min_len, flagUpper=False, flagLower=False, flagDigit=False):
    flagUpper_result = False
    flagLower_result = False
    flagDigit_result = False
    if min_len <= len(input_string):
        if flagUpper:
            for char in input_string:
                if char.isupper():
                    flagUpper_result = True
        else:
            flagUpper_result = True
        
        if flagLower:
            for char in input_string:
                if char.islower():
                    flagLower_result = True
        else:
            flagLower_result = True

        if flagDigit:
            for char in input_string:
                if char.isdigit():
                    flagDigit_result = True
        else:
            flagDigit_result = True
        if not flagDigit_result:
            print("Vas password mora da sadrzi bar jednu cifru")
        if not flagLower_result:
            print("Vas password mora da sadrzi bar jedno malo slovo")
        if not flagUpper_result:
            print("Vas password mora da sadrzi bar jedno veliko slovo")
        return flagUpper_result and flagLower_result and flagDigit_result
    else:
        return False

print(check_password("Passwadadad", 7, True, False, False))

def validacija_kartice(kartica):
    lista = []
    broj_kartice = str(kartica)
    if len(broj_kartice) == 16:
        for i, v in enumerate(broj_kartice):
            v = int(v)
            if i % 2 == 0:
                if v * 2 > 9:
                    doubled = v * 2
                    nova_cifra = (doubled // 10) + (doubled % 10)
                    lista.append(nova_cifra)
                else:
                    lista.append(v*2)
            else:
                lista.append(v)
        suma = 0
        for i in lista:
            suma += int(i)
        if suma % 10 == 0:
            return "Vasa kartica je validna"
        else:
            return "Vasa kartica nije validna"
    else:
        return "Vasa kartica nije validna. Ima " + str(len(broj_kartice)) + " cifara."

with open("cc_info.txt", newline="") as f:
    kartice = f.read().split("\n")
    for kartica in kartice:
        try:
            cc_number = int(kartica)
            print(validacija_kartice(cc_number))
        except Exception as e:
            print("Vasa kartica mora da sadrzi samo cifre.")