# ta funkcja zwraca pbliczoną wartość
def give_square(x):
    # słówko return zwraca wartość
    return (x**2)

# aby wartość zwrócona przez funkcją była możliwa do uzycia
# musimy ją zapisać do zmiennej
y = give_square(5)
print(y)
print(y * 2)

# możemy też wywołać funkcję jako argument innej funkcji
# tutaj wywołujemy funkcję give_square i jej zwrócona
# wartosć jest od razu przekazana do funkcji print
print(give_square(345))
print(give_square(34))
print(give_square(4))