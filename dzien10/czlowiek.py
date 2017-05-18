from dzien10.zwierze import Zwierze

class Czlowiek(Zwierze):
    """Klasa Człowiek jest podklasą klasy Zwierze
    Czlowiek dziedziczy zmienne i metody z klasy Zwierze"""
    def __init__(self, imie):
        """Inicjalizuje nową instancję Czlowieka"""

        # tutaj przekazujemy imie do rodzica, bo w nim
        # jest zadeklarowana zmienna imie
        # poniżej tworzymy instancję klasy Zwierze
        # czyli de facto - tworząc Człowieka,
        # on sam tworzy się jako Zwierze
        # to jest polimorfizm - jeden obiekt może być dwóch typów
        Zwierze.__init__(self, imie)

    def biega(self):
        """Bieganie ludzkie. Ta metoda nadpisuje implementacje
            zdefiniowaną w klasie rodzica.
            Instancja Czlowieka będzie korzystać z tej funkcji
            :arg nie z tej w Zwierze"""
        print("Człowiek {} biega".format(self.imie))


