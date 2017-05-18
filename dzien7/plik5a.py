# ta formułą sama dba o zamknięcie pliku
with open("mojplik.txt") as plik:
    # blok kodu, pamiętam o zagłebieniu
    print(plik.read())

print("Nie musze pamietac o zamknieciu!")