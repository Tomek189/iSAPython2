# otwieramy plik
# pamiętamy, ze przy scieżkach musimy escape'ować
# backslashe
plik = open("c:\\iSAPython2\\dzien7\\mojplik.txt")

# czytamy jedną linijkę
linijka = plik.readline()
print(linijka)

# pamietamy o zamykaniu plików
plik.close()
