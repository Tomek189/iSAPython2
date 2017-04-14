# haslo musi miec min 6 znaków, litery lub cyfry

# login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

while len(haslo) < 6:
        print("Hasło jest za krótkie! ", end="")
        print("Podaj prawidłowe hasło")
        haslo = input("Podaj prawidłowe hasło: ")

while not haslo.isalnum():
    print("Hasło musi miec litery i cyfry!")
    haslo = input("Podaj odpowiednie hasło: ")

print("Podano prawidłowe hasło!")

