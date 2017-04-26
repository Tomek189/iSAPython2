# lista imion
lista = ["Ala", "Ola", "Jola"]

# plik nie istnieje
# otwieramy w trybie w lub a
with open("imiona.txt", "w") as plik:
    # to zapisze elementy jednum ciągiem:
    # AlaOlaJola
    # plik.writelines(lista)

    for element in lista:
        plik.write(element + "\n")