# krotki

x = "jeden"
print(type(x))

# jednoelementowy tuple - pamiętamy o przecinku na końcu
y = "jeden",
print(y, type(y))

# pamiętamy o przecinku nawet gdy używamy nawiasów!!
y2 = ("igrek dwa",)
print(y2, type(y2))

z = ("dwa", "trzy", 5,6,7)
print(z)
print(type(z))

# tuple jest typem niezmiennym
# z[0] = "jeden"

for (indeks, element) in enumerate(z):
    print(indeks, element)

