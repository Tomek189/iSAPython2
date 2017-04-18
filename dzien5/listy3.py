# kolejka - pierwsze weszło pierwsze wyszło
# FIFO - first in first out
kolejka = []

# append() dodaje nowy element na końcu listy
kolejka.append(1)
print("Kolejka:", kolejka)
kolejka.append(56)
print("Kolejka:", kolejka)
kolejka.append(23)
print("Kolejka:", kolejka)

# pop(0) usuwa element z poczatku listy
print("Usuwam pierwszy element:", kolejka.pop(0))
print("Kolejka:",kolejka)
print("Usuwam pierwszy element:", kolejka.pop(0))
print("Kolejka:",kolejka)

print("\n---------------------\n")

# stos - ostatnie weszło pierwsze wyszło
# LIFO - last in first out
stos = []

# stos dodaje element na koniec listy
stos.append(1)
print("Stos:", stos)
stos.append(56)
print("Stos:", stos)
stos.append(23)
print("Stos:", stos)

# pop() usuwa element z końca listy
print("Usuwam ostatni element:", stos.pop())
print("Stos:", stos)
print("Usuwam ostatni element:", stos.pop())
print("Stos:", stos)
