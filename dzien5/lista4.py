lista = ["kwiatek", "woda", "doniczka", "ziemia"]

# element do usunięcia
el_to_remove = "kwiatek"

lista.remove(el_to_remove)
print(lista)

# element już usunięty, kolejna próba usunięcia
# spowoduje błąd
# lista.remove(el_to_remove)

# sprawdź najpierw czy element jest w liście, jeśli tak
# to usuń
if el_to_remove in lista:
    lista.remove(el_to_remove)
