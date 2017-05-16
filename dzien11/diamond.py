class Animal(object):
    """Klasa Animal"""
    def __init__(self, imie):
        """Inicjalizuje nowy obiekt"""
        self.name = imie

    def say(self):
        """Zwierze mówi"""
        print("Zwierzak {} nie mówi".format(self.name))

    def capitalize_name(self):
        """Kapitalizuje imie zwierzecia"""
        self.name = str(self.name).capitalize()

class Horse(Animal):
    """Koń - klasa pochodna od klasy Animal"""
    def __init__(self, imie):
        """Inicjalizuje nowy obiekt typu Koń"""

        # super() - oznacza rodzica
        super().__init__(imie)
        # inicjalizując obiekt powinniśmy użyć init z rodzica

    def say(self):
        """Własna implementacja mowy konia
        Ta metoda nadpisuje implementację z klasy Animal"""
        print("{} rży!".format(self.name))

    def jump(self):
        """Metoda specyficzna dla konia
        Nie jest ona dostępna w górę hierarchii"""
        print("Koń {} skacze!".format(self.name))


class Donkey(Animal):
    """klasa Osioł"""
    def __init__(self, imie):
        """Inicjalizuje nowy obiekt typu Donkey"""

        # znowu używamy inicjalizator z rodzica ale jawnie zadeklarowany
        Animal.__init__(self, imie)

    def say(self):
        """Własna implementacja mowy Osłą, nadpisuje
        to co jest w klasie rodzica czyli w Animal"""
        print("iiiiiiiiiiihahahhaaaaaa jestem osioł")

    def run(self):
        """Specyficzna metoda dla klasy Osioł"""
        print("Jestem uparty, ja nie biegam!")


class Mule(Horse, Donkey):
    """Klasa Muł - hybryda bo dziedziczy z Konia i Osła
    Ważna jest kolejność zdefiniowania rodziców - Python w 
    pierwszej kolejności będzie wyszukiwać elementy w Horse a potem w Donkey"""

    def say(self):
        """Własna implementacja mowy muła"""
        print("Muł mówi coś takiego:", end="")

        # odwołanie poprzez super() uruchomi metodę say() zdefiniowaną w pierwszym
        # rodzicu szukając od lewej do prawej strony w hierarchii dziedziczenia

        # super().say()

        # odwołanie się po nazwie klasy do jakiejś metody
        # spowoduje, że z tej konkretnej metody zostanie urichomiony kod
        # Donkey.say(self)
        Animal.say(self)


zwierz = Animal("ciasteczkowy potwór")
zwierz.capitalize_name()
zwierz.say()
print()
kon = Horse("gniady")
kon.capitalize_name()
kon.say()
kon.jump()

# zwierz nie może skakać bo jump() jest zdefiniowane niżej w hierarchii
# dziedziczyć mogą dzici od rodzicó (klasy pochodne od klas nadrzędnych)

# zwierz.jump()

print()
osiol = Donkey("Uparciuch")
osiol.capitalize_name()
osiol.say()
osiol.run()
print(osiol.name)

# run() zdefiniowane jest u osła a więc na tym samym poziomie
# rodzeństwo nie może dziedziczyć od siebie

# kon.run()

mul = Mule("muł edek")
mul.capitalize_name()

# muł korzysta ze wszystkich metod - od rodziców (Horse, Donkey)
# oraz od dziadka (Animal)
mul.say()
mul.run()
mul.jump()
