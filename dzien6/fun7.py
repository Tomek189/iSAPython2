# funkcja zwracająca odwrócony string
def odwroc_str(zdanie):
    return zdanie[::-1]

# tutaj wartość zwraca jest najpierw zapisana do zmiennej
# odwrocony = odwroc_str("Ala ma kota")
# print(odwrocony)

# a tutaj od razu wynik dziłania odwroc_str
# przekazujemy do funkcji print
# print(odwroc_str("Stół z powyłamywanymi nogami"))


def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return zdanie[::-1]

# print(odwroc_input())
# print(odwroc_input())