import pickle

with open("mojplik.txt") as plik:

    list_lines = plik.readlines()

    with open("lista.pickle", "wb") as zapis:
        pickle.dump(list_lines, zapis)



with open("lista.pickle", "rb") as ogorek:
    kiszony = pickle.load(ogorek)
    print(type(kiszony))
    print(kiszony)