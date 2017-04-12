# czy liczba jest podzielna przez 3, 5, lub 7

# input
liczba = input("Podaj liczbę: ")
# spr czy tylko cyfry
if liczba.isdigit():
    # jesli podzielna 3
    if int(liczba) % 3 == 0:
        print("Liczba jest podzielna przez 3")

    # w prz. razie czy podzielna przez 5
    elif int(liczba) % 5 == 0:
        print("Liczba podzielna przez 5")
    elif int(liczba) % 7 == 0:
        print("Liczba podzielna przez 7")

else:
    print("Podaj liczbę!!!")