# docstring - czyli dokumentacja naszej funkcji

def czy_w_zakresie(liczba, zakres):
    """ Sprawdza czy podana liczba jest w zakresie. Zwraca True jeśli jest.
    
    (liczba) -> bool
    """
    if liczba in zakres:
        return True
    else:
        return False

x = 23
y = range(1,24)
wynik = czy_w_zakresie(x, y)

print(wynik)

liczby = [23,345,22465,454,3543,34,35]

for liczba in liczby:
    # kolejny przykład reużywalności
    # w pętli wywołujemy raz napisany kod
    print(czy_w_zakresie(liczba, range(100000)))

