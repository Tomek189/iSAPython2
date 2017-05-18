class Pracownik(object):

    roczna_podw = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None
        Pracownik.ilosc_pracownikow += 1

    def ustaw_pensje(pesel, kwota):
        if kwota > 10000:
            pesel.wynagrodzenie = 10000
        else:
            pesel.wynagrodzenie = kwota

    def daj_podwyzke(self):
        self.wynagrodzenie += self.wynagrodzenie * (self.roczna_podw / 100)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)

    @classmethod
    def ustaw_roczna_podw(cls, ilosc_p_proc):
        cls.roczna_podw = ilosc_p_proc

    @classmethod
    def Pracownik_wynagr(cls, imie, stanowisko, pensja):
        """Alternatywny inicjalizator
        
        (imie, stanowisko, pensja) -> Pracownik"""

        # najpierw tworzymy obiekt za pomocją __init__
        prac = Pracownik(imie, stanowisko)
        # teraz możemy go dostosować
        prac.ustaw_pensje(pensja)
        # a na końcu zwrócić
        return prac

    # to jest metoda statyczna - nie korzysta ona z
    # informacji w instancji ani w klasie
    # klasy statyczne są wykorzystane jako metody pomocnicze
    # które logicznie powiązane są z klasą
    # używamy dekoratora @staticmethod
    @staticmethod
    def sprawdz_pesel(pesel):
        if len(str(pesel)) != 11:
            print("Pesel nieprawidłowy")

# metody statyczne wywołujemy podając
# nazwę klasy kropkę oraz nazwę metody
# nie musimy tworzyć instancji aby użyć taką metodę
Pracownik.sprawdz_pesel(987463547111)

print()
prac1 = Pracownik("adam", "kowal")

# tworzymy instancję za pomocą alternatywnego sposobu
prac2 = Pracownik.Pracownik_wynagr("Jakub", "spawacz", 5000)

prac1.ustaw_pensje(232323)

print(prac1)
print(prac2)


