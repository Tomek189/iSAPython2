plik = open("mojplik.txt")

print("To jest pierwsza linijka:")

print(plik.readline(), end='')

tresc = plik.read(16)
print(tresc)


plik.close()