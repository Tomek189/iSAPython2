# list comprehension

lista = [1,2,3,4,5,6,7,8,9]
lista2 = []

for element in lista:
    lista2.append(element**2)
# print(lista2)

# poniższe polecenie jest równoznaczne z powyższą
# pętlą for
lista3 = [element**2 for element in lista]
print(lista3)

lista4 = [element**2 for element in lista if element%3 == 0]
print(lista4)