# dict
slownik = {}

print(slownik)
print(type(slownik))

slownik2 = {'imie':'Adam', 'nazwisko':'kowalski', 1:'jedyneczka'}

# tuple jako typ niezmienny może być kluczem
slownik3 = {("jeden", "dwa"):[1,2,3,4,5,56]}
# print(slownik2)
# print(len(slownik2))
#
# print(slownik2[1])

print(slownik3[("jeden", "dwa")])

# kolekcje można zagnieżdżać
lista_slownikow = [{"nazwisko":"Kowalski"}, {}]

slownik5 = {3435:{"klucz wew":"wartosc wew"}}
print(slownik5[3435])

print(slownik2.keys())
print(slownik2.values())

# dodajemy klucz i wartość
#jeśli taki klucz istnieje to zmieniamy jego wartość
# jeśli nie istnieje to zostanie dodany do słownika
slownik2['wiek'] = 32

print(slownik2)

# usuwanie klucza i wartości
del slownik2['wiek']
print(slownik2)
