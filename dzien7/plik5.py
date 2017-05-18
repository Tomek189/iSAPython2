plik = open("mojplik.txt")

# czytamy jedną linijkę
# albo kilka
l = plik.readline()
print(l)

# a teraz czytamy pozostałą część do końca
reszta_pliku = plik.read()
print("To jest reszta:\n", reszta_pliku)

plik.close()

