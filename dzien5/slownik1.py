# dict

slownik = {}

print(slownik)
print(type(slownik))

slownik2 = {'imie':'Adam', 'nazwisko':'kowalski', 1:'jedyneczka'}
slownik3 = {("jeden", "dwa"):[1,2,3,4,5,56]}
# print(slownik2)
# print(len(slownik2))
#
# print(slownik2[1])

print(slownik3[("jeden", "dwa")])

lista_slownikow = [{"nazwisko":"Kowalski"}, {}]

slownik5 = {3435:{"klucz wew":"wartosc wew"}}
print(slownik5[3435])

print(slownik2.keys())
print(slownik2.values())
slownik2['wiek'] = 32

print(slownik2)

del slownik2['wiek']
print(slownik2)
