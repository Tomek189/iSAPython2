# czy liczba jest podzielna przez 3, 5, lub 7

# input
liczba = input("Podaj liczbę: ")
podzielnik = input("Podaj podzielnik: ")

# spr czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():
    # jesli podzielna 3
    if int(liczba) % int(podzielnik) == 0:
        print("Liczba jest podzielna przez ", podzielnik)
    else:
        print("Liczba nie jest podzielna przez", podzielnik)
        print("Wynik dzielenia:", int(liczba) / int(podzielnik))
else:
    print("Podaj liczbę!!!")