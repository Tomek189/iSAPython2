# w trybie w lub r+ kursor ustawi się na początku
# zawartości pliku
with open("mojplik.txt", "r+") as plik:
    # czytamy więc zawartość i w ten sposób
    # przemieszczamy kursor na koniec pliku
    zawartosc = plik.read()

    # sprawdzamy ostatni znak w pliku
    # jeśli będzie to \n to wiemy, że kursor zacznie
    # wpisywać od nowej linijki
    if zawartosc[-1] == '\n':
        plik.write("Dane zapisane do pliku.")

    # w innym przypadku, kursor znajduje się
    # na końcu ostatniej linijki, musimy więc
    # wstawić \n do dopisywanego stringa
    else:
        plik.write("\nDane zapisane do pliku.")


# w trybie 'a' też powinniśmy sprawdzić czy dopisujemy
# w nowej linijce czy w ostatniej

