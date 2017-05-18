# jesli chcemy jako argument domyśłny mieć typ mutowalny
# to jako wartość określamy None
def dodaj_imie(imie, imiona=None):
    # sprawdazmy czy jest domyślna wartość
    if imiona is None:
        # jeśli tak, to tutaj inicjalizujemy obiekt
        imiona = []
    imiona.append(imie)
    return imiona

# widzimy, że każde wywołanie tworzy nową listę
lista1 = dodaj_imie("Ola")
lista2 = dodaj_imie("Ala")
print(lista1)
print(lista2)

dodaj_imie("Piotrek", lista1)
print(lista1)