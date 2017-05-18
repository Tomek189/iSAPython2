from dzien10.ogloszenie import Ogloszenie

ogloszenia = []

ad1 = Ogloszenie(800, 40, "Gdańsk", "3434343")

ad1.wyswietl()

ad2 = Ogloszenie(2300, 60, "Gdańsk", 2342342)

ogloszenieXXX = Ogloszenie(232, 32, "Sopot", 3434)

for i in range(3):
    cena = input("Podaj cene")
    metraz = input("Podaj metraz")
    miasto = input("Podaj miasto")
    tel = input("Podaj tel")

    o = Ogloszenie(cena, metraz, miasto, tel)
    ogloszenia.append(o)

