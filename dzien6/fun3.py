# funkcja z dwoma wymaganymi argumentami
def drukuj_kwadraty(od, do):
    for l in range(od, do):
        print(l**2)

# wywołujemy funkcję
drukuj_kwadraty(23, 4556)

# oba argumenty są wymagane, wiec nie można uruchomić funkcji
# podając tylko jeden argument
drukuj_kwadraty(234)