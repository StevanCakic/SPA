from random import randrange, random
a = random()
# print(a)
a = random()
# print(a)
for i in range(100):
    pass
    # print(random())

print("Ocekivanje")
print(1/6)
br1 = br2 = br3 = br4 = br5 = br6 = 0

broj_eskperimenata = 100

for i in range(broj_eskperimenata):
    rezultat = randrange(1, 7)
    if rezultat == 1:
        # br1 += 1
        br1 = br1 + 1
    if rezultat == 2:
        br2 = br2 + 1
    if rezultat == 3:
        br3 = br3 + 1
    if rezultat == 4:
        br4 = br4 + 1
    if rezultat == 5:
        br5 = br5 + 1
    if rezultat == 6:
        br6 = br6 + 1

'''
print(br1, br2, br3, br4, br5, br6)
print(br1/broj_eskperimenata, br2/broj_eskperimenata, br3/broj_eskperimenata,
 br4/broj_eskperimenata, br5/broj_eskperimenata, br6/broj_eskperimenata)
'''

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA,winsB = simNGames(n, probA, probB)
    print("Broj pobjeda igraca A:", winsA)
    print("Broj pobjeda igraca B:", winsB)

def printIntro():
    print("Ovaj program simulira igru skvos izmedju dva igraca")
    print("Prvog igraca zvacemo A, a drugog B. Sposobnost igraca ")
    print("se ogleda u vjerovatnoci  (broj izmedju 0 i 1) da pobijedi")
    print(" kada servira. Uvijek prvo servira igraca A.")

def getInputs():
    a = float(input("Kolika je vjerovatnoca da pobijedi igrac A?"))
    b = float(input("Kolika je vjerovatnoca da pobijedi igrac B?"))
    n = int(input("Unesite broj igara za simulaciju eksperimenta:"))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB: 
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while scoreA != 15 and scoreB != 15:
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

main()