# kopiowanie list z listami zagnieżdżonymi

# importujemy moduł copy
import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_kwiecien = [nabial, chemia]
print("kwiecien:", zakupy_kwiecien)

# tworzymy listę kopiując płytko
zakupy_maj = zakupy_kwiecien.copy()
print("maj:", zakupy_maj)

# kopiujemy listę używając list comprehension
zakupy_czerwiec = [x for x in zakupy_kwiecien]
print("czerwiec:", zakupy_czerwiec)

# tworzymy listę używając funkcji deepcopy, czyli
# tworzymy głęboką kopię - czyli kopiujemy wszystkie
# wartości, nawet z typów złożonych (referencyjnych)
# a nie ich referencje (wskaźniki/adresy do pamięci)
zakupy_lipiec = copy.deepcopy(zakupy_kwiecien)

zakupy_kwiecien[1].append("gąbka")
print(zakupy_kwiecien)
print(zakupy_czerwiec)
print(zakupy_lipiec)
