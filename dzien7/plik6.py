# tryb 'a' to tryb dopisywania
# w tym trybie kursor od razu znajduje się
# na końcu zawartości pliku

with open("mojplik.txt", "a") as plik:
    plik.write("Moja kolejna linijka!!!")

