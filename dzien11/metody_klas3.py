class Pracownik(object):

    roczna_podw = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None
        Pracownik.ilosc_pracownikow += 1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self):
        self.wynagrodzenie += self.wynagrodzenie * (self.roczna_podw / 100)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)


    # to jest metoda klasy - ma dekorator @classmethod
    # oraz jako pierwszy argument przyjmuje klasę (cls)
    @classmethod
    def ustaw_roczna_podw(cls, ilosc_p_proc):
        """Zmienia wartość rocznej podwyżki"""
        cls.roczna_podw = ilosc_p_proc


emp1 = Pracownik("John Turturo", "aktor")
emp1.ustaw_pensje(5000)
emp2 = Pracownik("John Travolta", "gwiazda")
emp2.ustaw_pensje(8000)

Pracownik.ustaw_roczna_podw(10)
emp2.roczna_podw = 9

emp1.daj_podwyzke()
emp2.daj_podwyzke()

print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)


