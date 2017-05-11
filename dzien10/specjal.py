# metody specjalne
from dzien10.ogloszenie import Ogloszenie

o1 = Ogloszenie(2000, miejscowosc="Sopot")
o2 = Ogloszenie(3000, miejscowosc="Gdynia")

# wywołujemy print() na obiekcie
# zdefiniowaliśmy własne zachowanie obiektu dla print()
# poprzez zdefiniowanie metody __str__
print(o1)
print(o2)
suma = o1 + o2

print("Suma wynosi:",suma)

del o1
print("obiekt o1 usunąłem")
print(o2.cena)
