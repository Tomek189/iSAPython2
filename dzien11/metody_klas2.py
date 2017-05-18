class Pracownik(object):

    # to są zmienne klasy (pola klasy)
    # informacje w nich zawarte są takie same dla
    # wszystkich instancji
    roczna_podw = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None

        # odwołujemy się do pól klas podając
        # nazwę klasy, kropkę, nazwę pola
        Pracownik.ilosc_pracownikow += 1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)




print("---Tworzymy pierwszego pracownika---")
emp1 = Pracownik("John Turturo", "aktor")
emp1.ustaw_pensje(5000)
print("ilość pracowników:", Pracownik.ilosc_pracownikow)
print("\n---Tworzymy drugiego pracownika---")
emp2 = Pracownik("John Travolta", "gwiazda")
print("ilość pracowników:", Pracownik.ilosc_pracownikow)
emp2.ustaw_pensje(8000)

print("\n---Wypisujemy informacje o pracownikach---")
print(emp1)
print(emp2)

print("\n---Sprawdzamy pole klasy roczna_podw różnymi sposobami---")
print("Poprzez klasę:", Pracownik.roczna_podw)
print("Poprzez pierwszą instancję:", emp1.roczna_podw)
print("Poprzez drugą instancję:",emp2.roczna_podw)

print("\n---Zmieniamy wartość rocznej podwyżki oprzez klasę---")
Pracownik.roczna_podw = 8
print("roczna_podw widoczna przez klasę:", Pracownik.roczna_podw)
print("roczna_podw widoczna przez pierwszego pracownika:",emp1.roczna_podw)
print("roczna_podw widoczna przez drugiego pracownika:",emp2.roczna_podw)

print("\n--- Sprawdzimy zawartość naszych obiektów ---")
print("--- Do tego użyjemy zmiennej specjalnej __dict__ ---")
print("--- Wypisuje ona słownik, w którym kluczami są nazwy zmiennych i funkcji, "
      "\n   a wartościami są albo wartości albo wskaźniki do pamięci ")
print("\n--- Klasa zawiera różne rzeczy - ma pole roczna_podw ---")
print(Pracownik.__dict__)

print("\n--- pierwsza instancja zawiera różne rzeczy - nie zawiera zmiennej roczna_podw ---")
print(emp1.__dict__)

print("\n--- druga instancja zawiera różne rzeczy - nie zawiera zmiennej roczna_podw ---")
print(emp2.__dict__)

print("\n---Instancje nie mają zmiennej roczna_podw, więc znajdują je na poziomie---")
print("---klasy, dlatego widzą to samo---")

print("\n---Zmieniamy wartość podwyżki dla drugiego pracownika na 12---")
emp2.roczna_podw = 12

print("roczna_podw widoczna przez klasę:", Pracownik.roczna_podw)
print("roczna_podw widoczna przez pierwszego pracownika:",emp1.roczna_podw)
print("roczna_podw widoczna przez drugiego pracownika:",emp2.roczna_podw)
print("drugi pracownik ma indywidualną wartość, dlaczego?")
print("ponieważ, w momencie określenia indywidualnej wartości dla tej instancji")
print("de facto, stworzyliśmy w tej instancji zmienną roczna_podw")
print("zobaczmy teraz raz jeszcze co jest wewnątrz klasy, pracownika1 i pracownika2:")
print("\nzawartość klasy: - jest poe podwyżka z wartością 8\n")
print(Pracownik.__dict__)
print("\nZawartość pierwszej instancji: - NIE ma zmiennej roczna_podw")
print(emp1.__dict__)
print("\nZawartość drugiej instancji: - pojawiła się zmienna roczna_podw")
print(emp2.__dict__)

print("\nUsuwamy pracownika 2 i sprawdzamy ilosć pracowników")
del emp2
print("ilość pracowników:", Pracownik.ilosc_pracownikow)

# print(emp1.__dict__)
# print(emp2.__dict__)