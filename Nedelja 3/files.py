# Fajlovi

# Prvi dio (read i seek)
'''
f = open("./files/file.txt")
# print(f.read())
# print(f.read())

# Zasto kad opet pozovemo read() ne stampa nista?

# f.seek(0)
# print(f.read())

# f.seek(0)
# print(f.readlines())

f.seek(0)
# Iteracija kroz fajl liniju po liniju
for line in f:
    print(line)

f.close() # zatvaranje fajla
'''

# Drugi dio (write, append i close)
'''
f = open("./files/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("./files/demofile2.txt", "r")
print(f.read())

f = open("./files/demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

'''

# Kratko o with
'''
with open("./files/file.txt") as f:
    data = f.read()
    print(data)
'''

# Brisanje fajlova i foldera

'''
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

import os
os.rmdir("myfolder") # za brisanje foldera

'''
