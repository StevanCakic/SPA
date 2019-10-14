# Prvi
def doors(n):
    lista = []
    for i in range(n):
        lista.append(0)
    
    for student in range(1, n + 1):
        for(i, door) in enumerate(lista):
            if (i + 1) % student == 0: 
                if door == 0:
                    lista[i] = 1
                else:
                    lista[i] = 0

    number_of_ones = 0
    for i in lista:
        if i == 1:
            number_of_ones += 1
    print(number_of_ones)


doors(5)


# Cetvrti
def validacija_kartice(broj_kartice):
    duplirani = []
    broj_kartice = str(broj_kartice)
    if len(broj_kartice) == 16:
        for i, v in enumerate(kartica):
            v = int(v)
            if i % 2 == 0:
                if v*2 > 9:
                    doubled = v * 2
                    novi_broj = (doubled % 10)+(doubled//10)
                    duplirani.append(novi_broj)
                else:
                    duplirani.append(v*2)
            else:
                duplirani.append(v)
        suma = 0
        for i in duplirani:
            suma += int(i)
        
        if suma%10 == 0:
            return "Vasa kartica je validna"
        else:
            return "Vasa kartica nije validna"
    else:
        return "Vasa kartica nije validna. Nema tacno 16 cifara"


with open("cc_info.txt",newline="") as f:
    kartice = f.read().split("\n") # nekad ne radi ovo sa newline, pa moramo ovako
    for kartica in kartice:
        try:
            cc_number = int(kartica)
            print(validacija_kartice(cc_number))
        except Exception as e:
            print("Nevalidno unesena kartica")
