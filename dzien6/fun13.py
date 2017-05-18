# funkcja sprawdzająca czy podany string jest palindromem

# import dzien6.fun7
# dzien6.fun7.odwroc_str()

# importujemy moduł (plik) z naszym kodem
# musimy podać ścieżkę - miejscem startowym jest
# główny folder projektu
from dzien6.fun7 import *

def czy_palindrom(fraza):
    """Sprawdza czy fraza jest palindromem"""
    # tutaj używamy naszą funkcje z modułu fun7
    odwrocona = odwroc_str(fraza)

    # jedna z wersji rozwiazania
    for litera1, litera2 in zip(fraza, odwrocona):
        if litera1 != litera2:
            return False

    return True

    # drugi sposób rozwiązania
    # for litera1, litera2 in zip(fraza, odwrocona):
    #     if litera1 == litera2:
    #         continue
    #     else:
    #         return False
    #
    # return True

print(czy_palindrom("kajak"))
print(czy_palindrom("Alamakota"))