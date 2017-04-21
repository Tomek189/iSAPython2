# jako argument domyślny dajemy typ zmienny - listę
def dodaj_imie(imie, imiona=[]):
    imiona.append(imie)
    return imiona

# wywołujemy funkcję, bez podawania argumentu domyślnego
lista_imion = dodaj_imie("Ola")
print(lista_imion)

# okazuje się, że kolejne wywołanie funkcji dodaje imie do
# listy utworzonej przy pierwszym wywołaniu
lista_imion2 = dodaj_imie("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie("Piotrek")
print(lista_imion3)

