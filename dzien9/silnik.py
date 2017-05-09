class Silnik(object):
    '''Silnik'''

    def __init__(self, pojemnosc, moc_KM, paliwo):
        """
        Inicjalizuje nowy obiekt typu Silnik
        :param pojemnosc: Pojemność silnika w cm3
        :param moc_KM: Moc silnika w KM
        :param paliwo: Rodzaj paliwa
        """
        self.V = pojemnosc
        self.KM = moc_KM
        self.paliwo = paliwo


def main():
    v6 = Silnik(5600, 600, "benzyna")
    print(v6.V)
    print(v6.KM)
    print(v6.paliwo)
    print(type(v6))

if __name__ == '__main__':
    main()