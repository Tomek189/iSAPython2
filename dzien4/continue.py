# continue
for i in range(100):
    if i % 35 == 0:
        #polecenie continue prerywa bieżacy krok pętli
        continue
    else:
        print(i)

# ta petla działa tak samo jak ta wyżej
for i in range(100):
    if i % 35 != 0:
        print(i)