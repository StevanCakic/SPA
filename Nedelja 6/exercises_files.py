# Zadatak 1: 
# Potrebno je izdvojiti/prikazati sve filmove cija je ocjena veca od unijete i 
# ciji je zanr filma odgovara unijetom zanru.

# Korisniku pri unosi napomenutu da su ocjene od 1 do 10, a osim toga
# treba napomenuti i koje zanrove moze da odabere.
# Ako korisnik unese podatke pogresno, treba da mu se prikaze greska i da mu se napomene
# da opet unosi novi input

# Napomena: Kreirati fajl filmovi.txt u kome se svaki film, pojedinacno, cuva u jednom redu,
# tj. ako imate unos od 5 filmova, fajl treba da sadrzi 5 linija. 
# Takodje, svaki film je opisan: nazivom, ocjenom, godina izlaska i zanrovima
    # Atributi filma odvojeni su sa ;
    # Naziv filma ne smije da ima vise od 50 karaktera, a ne manje od 2
    # Naziv filma pocinje sa velikim slovom
    # Ocjene su zaokruzeni float brojevi (od 1 do 10) na dvije decimale
    # Film moze da ima vise od jednog zanra, zanrovi su razdvojeni zarezima 

# Nakon filtriranja filmova, omoguciti korisniku da doda novi film (ne dozvoliti da unese pogresan)

# Preporuka, koristiti list comprehension, funkcija za konverziju stringa u torku je tuple
# Hint: tup = tuple(some_str.split(",")) - konvertuje npr. "abcd,abbccd" -> ("abcd","abbccd")

# Napisati funkciju za odabir filtera
# 1 - Po nazivu filma (pocetni term naziva)
# 2 - Po ocjeni (vece od)
# 3 - Po zanru

