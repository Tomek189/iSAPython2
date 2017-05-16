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

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)





emp1 = Pracownik("John Turturo", "aktor")
emp1.ustaw_pensje(5000)
print("ilość pracowników:", Pracownik.ilosc_pracownikow)

emp2 = Pracownik("John Travolta", "gwiazda")
print("ilość pracowników:", Pracownik.ilosc_pracownikow)
emp2.ustaw_pensje(8000)
print(emp1)
print(emp2)

print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)

Pracownik.roczna_podw = 8
print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)
print()
emp2.roczna_podw = 12
print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)

del emp2
print("ilość pracowników:", Pracownik.ilosc_pracownikow)

# print(emp1.__dict__)
# print(emp2.__dict__)