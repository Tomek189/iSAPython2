# petla for

# range zwraca zakres (zbiór liczb całkowitych)
x = range(100)
print(x)

for liczba in range(100):
    print(liczba * liczba)


for litera in "Aleksandra"[::-1]:
    print(litera)

for litera in "Aleksandra":
    print(litera.capitalize())

# zmienną lokalną pętli nie musze wykorzystywać w kodzie pętli
# w tym wypadku spełniać ona będzie wyłącznie funkcje licznika pętli
for litera in "Aleksandra":
    print("Nie korzystam ze zmiennej litera!")

imie = "Hermenegilda"
# indeks = 0
#
# for c in imie:
#     print(indeks, c)
#     indeks += 1

# enumerate zwraca dwie wartości:
# indeks elementu w kolekcji oraz
# wartość elementu pod tym indeksem
# for i, c in enumerate(imie):
#     print(i, c)









