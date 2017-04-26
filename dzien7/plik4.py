plik = open("mojplik.txt")

linijki = plik.readlines()

print(linijki)

for linijka in linijki:
    print(linijka, end='')

plik.close()