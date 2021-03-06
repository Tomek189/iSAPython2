# listy
# deklarowanie list

# listy tworzymy za pomocą []
lista = ["trzy", "jeden"]

# w listach mogą być duplikaty
lista1 = [2, 3, 4, 9, 0, 3, 4]
print(lista1)
print(type(lista1))

# możemy stworzyć za pomoca funkcji list()
lista2a = list("kwiatek")
print(lista2a)

lista2 = list(["kwiatek", "doniczka"])
print(lista2)

# tworzymy str zawierający wszystkie elementy listy, połączone znakiem ''
# czyli pustym stringiem
# mozemy tu użyć dodowlnego znaku
el_string = ''.join(lista2)
print(el_string)
print(type(el_string))

# różne typy w liście
# listy możemy zagnieżdżać
lista3 = [1, "dwa", 3.0, range(3), [0, 1]]
print(lista3)
print(len(lista3))
print(lista3[2])

# aby dostać się do elementu w liście zagnieżdźonej stosujemy
# indeksowanie wielokrotne
print(lista3[4][0])

# w przeciwieństwie do list, stringi są niemutowalne
# imie = "Ala"
# imie[0] = "O"
# # stringi są immutable, nie mogę ich zmienic
# print(imie)

lista3[1] = "osiem"
print(lista3)
