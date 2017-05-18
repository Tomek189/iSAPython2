from dzien10.zwierze import Zwierze
from dzien10.czlowiek import Czlowiek
from dzien10.student import Student

# obiekt Zwierze
animal1 = Zwierze("mamut")
# obiekt Człowiek
animal2 = Czlowiek("Janek")

# imie zdeklarowaliśmy w klasie Zwierze
print(animal1.imie)
# Człowiek dziedziczy z klasy Zwierze
# więc też ma imie
print(animal2.imie)

# metoda biega() określona jest w klasie Zwierze
animal1.biega()
# Czlowiek ma wlasną implementacje metody biega()
animal2.biega()

# w ten sposób możemy spowodować
# aby obiekt Czlowiek nie używał własnej
# metody biega(), tylko z klasy Zwierze
Zwierze.biega(animal2)

# obiekt student, ma specyficzną dla siebie informację
# zmienna nr_indeksu jest zdefiniowana w klasie Student
# nie jest więc ona widoczna w górę hierarchii
student1 = Student("Janek", 43344)
print(student1.nr_indeksu)

# klasa człowiek nie ma pola nr_indeksu
# to pole ma Student, ale rodzic nie widzi tego co ma dziecko
#animal2.nr_indeksu
