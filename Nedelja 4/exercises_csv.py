import csv

with open("../assets/google_stock_data.csv", newline="") as file: # newline zbog /n kod nekih OS
    reader = csv.reader(file)
    header = next(reader) # Ucitaj prvi red
    print(header)
    print("datetime", "float", "  float", "  float", "  float", "  integer", "   float")

    # Konverzija tipova

    from datetime import datetime
    result = []

    for row in reader:
        date = datetime.strptime(row[0], "%m/%d/%Y")
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])
        result.append([date, open_price, high, low, close, volume, adj_close])

    print(result[0])


    # Zadatak da izracunamo stock daily return, 
    # tj. procentualnu razliku za dva susjedna dana (adj close) 100 * [( A - B) / B]
    # U novom fajlu trebamo da imamo dvije kolone i to: Date i stock daily return (in perc)
    # Cesto se trazi da se ovo racuna osim po danima, i po nedeljama, mjesecima, godinama
    # Vremeno cemo nauciti kako se to radi




    
