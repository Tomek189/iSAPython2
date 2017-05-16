# zmień stringa w listę wyrazów (przecinki usuwamy)

zdanie = "Ala ma kota, kot ma ale"
zdanie = zdanie.replace(',', '')

lista = zdanie.split()
print(lista)