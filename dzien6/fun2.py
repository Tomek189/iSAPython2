# definiowanie z argumentami

def drukuj_kwadraty():
    liczby = range(12)
    for l in liczby:
        print(l**2)

# nie można zadeklarować dwa razy tej samej funkcji
# jesli to zrobimy to ostatnia deklaracja będzie ważna
# nie będzie można wywołać funkcji drukuj_kwadraty()
# bo została nadpisana przez funkcję przyjmującą 1 argument
# dlatego ta funkcja powinna nazywać się inaczej
def drukuj_kwadraty(max_num):
    for l in range(max_num):
        print(l**2)


drukuj_kwadraty(10)
drukuj_kwadraty(100)
drukuj_kwadraty(3242)
