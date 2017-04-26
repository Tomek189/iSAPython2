plik = open("mojplik.txt")

l = plik.readline()
print(l)

reszta_pliku = plik.read()
print("To jest reszta:\n", reszta_pliku)

plik.close()

