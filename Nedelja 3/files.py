# Fajlovi

# Prvi dio (read i seek)

# kreirati folder files u folderu Nedelja 3, a u njemu fajl file.txt da bi program normalno radio
f = open("./files/file.txt")
print(f.read())
print(f.read())


# Zasto kad opet pozovemo read() ne stampa nista?

f.seek(0)
print(f.read())

f.seek(0)
print(f.readlines())


f.seek(0)
# Iteracija kroz fajl liniju po liniju
for line in f:
    print(line)

f.close() # zatvaranje fajla


# Drugi dio (write, append i close)

f = open("./files/demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()


#open and read the file after the appending:
f = open("./files/demofile2.txt", "r")
print(f.read())


f = open("./files/demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

'''
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

'''

# Kratko o with
# koristi se za context, fajl otvoren sa with automatski se zatvari van with bloka
with open("./files/file.txt") as f:
    data = f.read()
    print(data)


# Brisanje fajlova i foldera

'''
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# prolazimo kroz folder files
for file in os.listdir("./files"):
    # brisemo fajlove redom
    os.remove("./files/" + file)

# direktorijum je moguce obrisati samo ako nema fajlova
os.rmdir("./files") # za brisanje foldera

'''


