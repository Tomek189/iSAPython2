# czy liczba jest podzielna przez 3, 5, lub 7

# input
liczba = input("Podaj liczbę: ")
podzielnik = input("Podaj podzielnik: ")

# spr czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():

    wynik = int(liczba) / int(podzielnik)
    # print(wynik)

    if round(wynik, 2).is_integer():
        print("Liczba {0} jest podzielna przez {1}".format(liczba, podzielnik))
    else:
        print("Liczba {} nie jest podzielna przez {}".format(liczba, podzielnik))
        print("Wynik dzielenia: {:.2f}".format(wynik))

else:
    print("Podaj liczbę!!!")