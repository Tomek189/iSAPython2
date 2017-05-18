# wbudowany moduł do pracy z plikami csv
import csv

# odczytanie csv
with open("osoby.txt") as plik:
    # tworzymy czytnik
    czytnik = csv.reader(plik)

    for line in czytnik:
        # jak widzimy linia jest już listą z elementami
        print(line)

dane = ["Bartosz", "Mojo", 33]

with open("osoby.txt", "a") as plik:
    # tworze zapisywacz
    zapisywacz = csv.writer(plik)
    zapisywacz.writerow(dane)











