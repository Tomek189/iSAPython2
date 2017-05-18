
try:
    with open("dane.txt") as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e)
    print("Podany plik nie istnieje")
except Exception:
    print("Pojawił się błąd!!!!")

print("Dalsza cześć programu")

