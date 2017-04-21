# mozemy miec kilka argumwntów wymaganych i domyslnych
# imie i nazwisko są argumentami wymaganymi
# kurs i ilosc_dni są argumentami domyślnymi - nie trzeba ich
#   podawać przy wywołąniu funkcji
# WAZNE!!! Argumenty domyślne muszą być definiowane po wymaganych
def wypisz_dane(imie, nazwisko, kurs="Python", ilosc_dni=15):
    print(imie, nazwisko, kurs, ilosc_dni)

# wywołanie funkcji z argumentami wymaganymi
wypisz_dane("Arek", "g")

# wywołanie z arg. wymaganymi i pierwszym arg. domyślnym
wypisz_dane("Anna", "Kowalska", "Java")

# wywołujemy z arg. wymaganymi i wszystkimi domyślnymi
wypisz_dane("Adam", "kowalski", "JavaScript", 20)

# jesli chcemy podać drugi w kolejności argument domyślny,
# to musimy podać jego nazwę oraz przypisać wartość
# Python bierze pod uwagę kolejność argumentó i przypisuje
# do nich odpowiednie wartośći, aby zmienić kolejność musimy
# zrobić to jawnie - podając konkretne argumenty
wypisz_dane("Marek", "Zegarek", ilosc_dni=30)

# możemy zmieniać kolejność wszystkich argumentów
# również wymaganych - ale musimy podawać ich nazwy
wypisz_dane(ilosc_dni=34, imie="Joanna", kurs="JS", nazwisko="Nowak")

