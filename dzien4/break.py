# break

imie = "Hermenegilda"

for litera in imie:
    if litera == 'n':
        # break zatrzymuje działanie całej pętli
        break
    print(litera)

print("koniec")

imie2 = "Agnieszka"

# zip() daje nam możliowść poruszania się po elementach dwóch
# lub więcej kolekcji równocześnie
for litera1, litera2 in zip(imie, imie2):
    print(litera1, litera2)


indeksy = '012345678911'
zdanie = 'Ala ma kota kot ma ale'

# jeśli kolekcje są różnej długości to z dłuższej kolekcji
# zostanie tylko tyle elementów co w krótszej
for i, l in zip(indeksy, zdanie):
    print(i, l)