# tu podaliśmy drugi argument - tryb otwarcia pliku
# 'r' - tylko do odczytu
# jeśli nie podamy tego argumentu, to domyślnie plik będzie
# otwarty w trybie 'r'
plik = open('mojplik.txt', 'r')

linijka = plik.readline()
print(len(linijka))

# sprawdzam pozcję kursora poleceniem tell()
print(plik.tell())

# seek() służy to przemieszczania kursora
# liczba oznacza numer znaku w pliku
# w trybie binarnym ozacza numer bajtu
plik.seek(0)

linijka = plik.readline()
print(linijka)

plik.close()