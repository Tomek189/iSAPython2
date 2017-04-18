# listy
# deklarowanie list

# lista = ["trzy", "jeden"]
# lista1 = [2, 3, 4, 9, 0, 3, 4]
# print(lista1)
# print(type(lista1))
#
# lista2a = list("kwiatek")
# print(lista2a)
# lista2 = list(["kwiatek", "doniczka"])
# print(lista2)
#
# el_string = ''.join(lista2)
# print(el_string)
# print(type(el_string))

lista3 = [1, "dwa", 3.0, range(3), [0, 1]]
print(lista3)
print(len(lista3))
print(lista3[2])
print(lista3[4][0])

# imie = "Ala"
# imie[0] = "O"
# # stringi są immutable, nie mogę ich zmienic
# print(imie)

lista3[1] = "osiem"
print(lista3)
