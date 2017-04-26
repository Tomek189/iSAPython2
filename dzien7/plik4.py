plik = open("mojplik.txt")

# readlines() zwraca listę linijek
linijki = plik.readlines()

print(linijki)

for linijka in linijki:
    # pamiętamy, że linijki mają na końcu \n
    # dlatego chcemy aby print() już nie wstawiał
    print(linijka, end='')

plik.close()