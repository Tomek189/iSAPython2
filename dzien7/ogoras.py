# pickle pozwala na zapisanie do pliku wszystkiego
import pickle

dane = ["Bartosz", "Mojo", 33]

# zapisanie obiektu do pliku
# pickle zapisze obiekt razem ze wszystkimi danymi
# które są w obiekcie
# pliki otwieramy w trybie 'b' - binarnym!!!
with open("ogorek.pickle", "wb") as plik:
    pickle.dump(dane, plik)

# odczytanie - pamiętamy o trybie binarnym!
with open("ogorek.pickle", "rb") as plik:
    dane_wczytane = pickle.load(plik)

print(dane_wczytane)
