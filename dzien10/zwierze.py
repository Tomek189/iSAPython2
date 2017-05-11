class Zwierze(object):
    """Klasa Zwierze, dziedziczy z klasy obiekt"""
    def __init__(self, imie):
        """Inicjalizuje obiekt Zwierze"""
        # ta zmienna instancji będzie dostępna
        # dla wszystkich potomnych klas:
        # dzieci, wnuków itd.
        # one nie muszą jej ponownie definiować
        self.imie = imie

    def biega(self):
        """Zwierze biega. Każda klassa dziedzicząca 
        z klasy Zwierze bedzie mogła użyć tej metody."""
        print("Zwierze {} biegnie".format(self.imie))
