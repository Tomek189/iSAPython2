osoba = ["pamela", "anderson", 50]

# przed zapisaniem danych do pliku w ten sposób
# musimy zamienić wszystkie typy na str()
# w innym przypadku będzie błąd
osoba_str = [str(dane) for dane in osoba]

# tworzymy stringa zawierającego elementy z listy
# przecinki będą wstawione między elementy
# jeśli uzyjemy tu zamist osoba_str listy osoba
# to otrzymamy błąd - tylko elementy będące str można .join()
dane_zapis = ",".join(osoba_str)

with open("osoby.txt", "a") as plik:
    plik.write(dane_zapis + "\n")

