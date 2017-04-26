
def kwadrat(a):
    return a**2

# ta funkcja zawiera kod w którym wykorzystujemy nasze zdefiniowane
# metody - jest to główna funkcja programu
def main():
    print(kwadrat(45))
    print(kwadrat(10))

# ten warunek sprawdza czy nasz plik(moduł)
# jest uruchamiany bezpośrednio, czy jest
# importowany do innego pliku
# jeśli będzie importowany, to funkcja main()
# nie wykona się automatycznie, trzeba będzie ją
# wywołać ręcznie
# natomiast jeśli plik uruchomimy bezpośrednio to
# main() zostanie wywołana

if __name__ == '__main__':
    main()

