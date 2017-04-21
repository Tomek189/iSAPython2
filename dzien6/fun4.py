# funkcja z argumentem domyślnym
def wypisz_imie(imie="arek"):
    imie = imie.capitalize()
    print(imie)

# przy wywołaniu tej funkcji, nie trzeba podawać argumentu
# w takim wypadku funkcja użyje wartości domyślnej określonej
# w jej definicji tj. "arek"
wypisz_imie()

# tu podajemy własny argument
wypisz_imie("ala")
wypisz_imie("marta")
wypisz_imie("aleksander")

