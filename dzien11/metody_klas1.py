class Pracownik(object):
    def __init__(self, imie, stanowisko):

        # to są zmienne instancji - poznajemy, że są one po
        # słówku self
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None

    # metody instancji ZAWSZE mają jako pierwszy argument,
    # oznaczający instancję (obiekt) oznaczone słowem self

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)

emp1 = Pracownik("John Turturo", "aktor")
emp2 = Pracownik("John Travolta", "gwiazda")
emp1.ustaw_pensje(5000)
emp2.ustaw_pensje(23423423)
print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)
emp1.daj_podwyzke(10)
emp2.daj_podwyzke(10)
print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)

# zmienne instancji są niezależne - każda instancja ma
# w nich swoje własne informacje

# metody instancji