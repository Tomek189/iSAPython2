# metody wbudowane
# aby zobaczyć jakie metody są dostępne to
# po nazwie zmiennej albo bezpośrednio po stringu piszemy kropkę
# wtedy PyCharm wyświetli okienko z dostępnymi metodami

osoba = "jan kowalski"

# stringi są typem niemutowalnym
# wywołanie metody nie powoduje zmiany oryginalnego stringa
print(osoba.capitalize())

# aby zachować to co metoda robi (oddaje zmienioną wartość - kopię stringa)
# musimy zwracaną wartość zapisać do zmiennej - może być ta sama
# ale wtedy oryginalna wartość przestaje istnieć
osoba = osoba.capitalize()

print(osoba)
# print(nowa_osoba)

print(osoba.endswith("ska"))
print(osoba.endswith("ski"))

print(osoba.find("a"))

# ord() zwraca numer kody z tablicy ASCII / UTF8
print(ord("a"))

# inne typy też mają swoje metody wbudowane:

print(float(5.0).hex())
print(float(5.0).is_integer())

