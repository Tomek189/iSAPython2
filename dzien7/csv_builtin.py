import csv

# odczytanie csv
with open("osoby.txt") as plik:
    # tworzymy czytnik
    czytnik = csv.reader(plik)

    for line in czytnik:
        print(line)

dane = ["Bartosz", "Mojo", 33]

with open("osoby.txt", "a") as plik:
    # tworze zapisywacz
    zapisywacz = csv.writer(plik)
    zapisywacz.writerow(dane)











