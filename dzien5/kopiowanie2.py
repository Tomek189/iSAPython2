import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_kwiecien = [nabial, chemia]
# print("kwiecien:", zakupy_kwiecien)

zakupy_maj = zakupy_kwiecien.copy()
# print("maj:", zakupy_maj)

zakupy_czerwiec = [x for x in zakupy_kwiecien]

# print("czerwiec:", zakupy_czerwiec)

zakupy_lipiec = copy.deepcopy(zakupy_kwiecien)

zakupy_kwiecien[1].append("gąbka")
print(zakupy_kwiecien)
print(zakupy_czerwiec)
print(zakupy_lipiec)
