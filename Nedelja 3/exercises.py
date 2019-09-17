# Zadatak 1
'''
    Napisati funkciju koja za unijeti string i slovo vraća sve riječi čija je dužina paran 
    broj, a ne sadrže zadato slovo (koje korisnik unosi). 
    Primjer: 
    get_even_word_filterd_by_letter(“Print every word in this sentence that has an even number of letters”, “d”) 
    vraća [“in”, “this”, “sentence”, “that”, “an” ,”even”, “number”, “of” ]
'''

# Zadatak 2
'''
Napisati funkciju koja za zadati segment [start, end] (uključujući start i end) kvadrira sve
elemente liste koji su djeljivi sa 3 ili djeljivi sa 2 ali ne sa 5, a onda ih sumira. 
Štampati sumu. 
Primjer: square_and_sum(1, 10) vraće 210 (2**2 + 3**2 + 4**2 + 6**2 + 8**2 + 9**2 = 210)
'''

# Zadatak 3
'''
    Klijenti postavljaju zahtjeve brokeru za kupovinu/prodaju akcija. Zahtjevi mogu da
    budu jednostavni ili višestruki (više jednostavnih). Zahtjev ima sledeći format:
    Quote /space/ Quantity /space/ Price /space/ Status
    gdje Quote predstavlja naziv akcije, sadrži non-whitespace karaktere, Quantity je prirodan broj koji predstavlja broj akcija koje se prodaju/kupuju, Price je double koji predstavlja cijenu pojedine akcije (sa decimalnom tačkom "." ), Status je B (buy) ili S (sell) koji predstavlja da li se akcije prodaju ili kupuju.
    Primjer 1 (simple):
    "GOOG 300 542.0 B"

    Višestruki zahtjevi se sastoje od više simple zahtjeva koji su spojeni zarezom
    Primjer 2 (multiple-višestruki):
    "ZNG 1300 2.66 B,CH15.NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"

    Da olakšate brokeru posao vaš zadatak je da mu vratite string "Buy: b Sell: s" gdje su b i s formata 'double' zaokruženog na 2 decimalse, b predstavlja ukupnu cijenubkupljenih akcija, a s ukupnu cijenu prodatih akcija.

    Output za primjer 2:
    "Buy: 29499.00 Sell: 0"

'''

# Zadatak 4
'''
Vaš program treba da nađe najdužu sekvencu izastopnih nula za unijetu listu. 
Takodje, treba da vrati pocetnu i krajnju poziciju te podliste u listi

Primjer:
Niz [1, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0] ima tri sekvence uzastopnih nula sa dužinama 3, 1 i 4. 
Vraca (4, 7, 10) gdje je 4 duzina podniza, 7 startna pozicija (ukljucuje),
10 krajnja pozicija (ne ukljucuje) 

'''