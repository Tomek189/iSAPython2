# kopiowanie list z typami prostymi
wynik = 3

# zmienna wynik zawiera typ wartościowy, więc
# w momencie tworzenia listy, jako element jest brana
# aktualna wartość zmiennej wynik
lista_a = ["zero", "jeden", wynik]
print("lista a:", lista_a)

# zmieniamy wartość zmiennej
wynik = 43
print("lista a po zmianie:", lista_a)
# lista_a posiada pierwotną wartość zmiennej wynik
print()

lista_b = lista_a.copy()
print("Lista b skopiowana z a:", lista_b)

print("Dodajemy element do listy a")
lista_a.append("nowy")

print(lista_a)
print(lista_b)

# id() zwraca adres pamięci
print(hex(id(lista_a)))
print(hex(id(lista_b)))