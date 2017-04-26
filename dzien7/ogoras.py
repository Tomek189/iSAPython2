import pickle

# dane = ["Bartosz", "Mojo", 33]

# with open("ogorek.pickle", "wb") as plik:
#     pickle.dump(dane, plik)

# odczytanie

with open("ogorek.pickle", "rb") as plik:
    dane_wczytane = pickle.load(plik)

    print(dane_wczytane)

