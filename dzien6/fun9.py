# zmienna na poziomie globalnym
imie = "jola"
# print(imie)

def drukuj_imiona(imie_2):
    # aby użyć zmiennej globalnej wew. funkcji musimy
    # użyć słówka global
    global imie
    print(imie)
    # zmienna imie jest globalna, bo użyliśmy global
    imie = "ania"
    imie = imie.capitalize()
    imie_2 = str(imie_2).capitalize()

    print(imie, imie_2)

drukuj_imiona("gosia")
print(imie)

