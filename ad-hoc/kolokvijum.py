def uvecajCifreZa1(string):
    result = ""
    for karakter in string:
        if karakter.isdigit():
            num = int(karakter)
            if num == 9:
                num = 0
            else:
                num += 1
            result += str(num)
        else:
            result += karakter

    return result

print(uvecajCifreZa1("Danas je 28.11.2019."))

def brojNeparneCifre(N):
    to_str = str(N)
    broj_neparnih_cifara = 0
    for cifra in to_str:
        if int(cifra) % 2 != 0:
            broj_neparnih_cifara += 1
    return broj_neparnih_cifara

print(brojNeparneCifre(31212))

def upis_u_fajl():
    f = open("brojevi.txt", "r")
    res = f.read().split("\n")
    f.close()
    f = open("rezultat.txt", "w")
    for broj in res:
        if len(broj) == 2 or len(broj) == 3:
            f.write("#" + broj + "#\n")
    f.close()
    

upis_u_fajl()