from dzien10.czlowiek import Czlowiek


class Student(Czlowiek):
    """Student dziedziczy z klasy Czlowiek"""
    def __init__(self, imie, indeks):
        """Własny inicjalizator Studenta
        """
        # tutaj inicjalizujemy studenta jako Czlowieka
        # super oznacza klasę nadrzędną (rodzica) - Python sam bedzie
        # wiedział jaka to kalsa
        super().__init__(imie)

        # Tutaj pojawia się specyficzna dla studenta zmienna:
        # numer indeksu.
        # Zwierze i Czlowiek nie potrzebują jej.
        # Dlatego najlepszym miejscem na jej deklarację jest klasa Student
        self.nr_indeksu = indeks