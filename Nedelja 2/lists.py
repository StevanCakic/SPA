# Liste

# Prvi dio
# Kreirajmo listu koja sadrži različite tipove podataka
# Isprobajmo indeksiranje i slicing
# Isprobajmo spajanje više listi u jednu
lista = [1, 10, "abc", [10, 10]]
print(lista[::-1])

# Drugi dio
# Metode za liste
# Isprobajmo ih redom

lista.append([100, 200, 300])
print(lista)
a = lista.pop(0)
print(a)
print(lista)

# Treci dio
# Kreirati matricu 3x3
# Kako biste izdvojili prvu vrstu matrice?
# A prvu kolonu?

matrix = [[1,2,3], [4,5,6], [7,8,9] ]
first_column = [row[0] for row in matrix]
print(first_column)

# Razlika između append i extend
list_a = [1, 2, 3]
list_a.append([4, 5])
print(list_a)

list_b = [1, 2, 3]
list_b.extend([4,5])
print(list_b)

# Četvrti dio
# Kreirajmo listu a, dodijelimi listi a listu b, i probajmo da dodamo element u listu b
# Štampati a, štampati b? Ako dodamo element u listu a dešava li se isto?
# Kako ovo da riješimo?

lista_a = [10, 20, 30]
lista_b = lista_a.copy()
lista_a[2] = 100
print(lista_a)
print(lista_b)
