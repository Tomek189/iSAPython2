lista = [1, "dwa", "trzy", 4]

# for element in lista:
#     print(element)

lista_z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(type(lista_z))

# iterowanie przez elementy w listach wewnętrznych
for element in lista_z:
    print("Obecny element: {} - typ: {}".format(element, type(element)))
    for subelement in element:
        print("Subelement: {} - typ: {} w elemencie: {} ".format(subelement, type(subelement), element))

# slicowanie list
print(lista[1:3])
print(lista)

# pop() usuwa element
x = lista.pop()
print(x)
print(lista)