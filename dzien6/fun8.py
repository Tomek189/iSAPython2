# zmienne lokalne i globalne
# ta zmienna jest na poziomie globalnym
imie = "ola"

def duza_litera(imie="ala"):
    # ta zmienna imie jest na poziomie lokalnym funkcji
    imie = imie.capitalize()
    # zmienna wiek lokalna funkcji
    wiek = 23
    return imie

print(duza_litera())
print(imie)
# na poziomie globalnym zmienna wiek nie istnieje
print(wiek)

