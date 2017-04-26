plik = open("mojplik.txt")

print("To jest pierwsza linijka:")

# w przypadku wczytywania zawartości plików
# na końcu linijek znajduje się znak nowej linii \n
# ten znak dla nas nie widoczny, dla komputera mówi
# ustaw się w nowej linijce
# w przypadku użycia print() - print dodaje na końcu stringa,
# który drukuje \n , więc w tym przypadku użycie print()
# na stringu, który już ma znak nowej linii spowoduje, wstawienie
# kolejnej nowej linii przez print(), dlatego określamy
# aby print() na koniec linii wstawiał pusty string - czyli nic
print(plik.readline(), end='')

# read() możemy podać ilość znaków do wczytania
tresc = plik.read(16)
print(tresc)

plik.close()
