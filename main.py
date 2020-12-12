print('4.1')
with open('liczby.txt') as liczby:
    zera = 0
    for liczba in liczby:
        licznik_0 = 0
        licznik_1 = 0
        for cyfra in liczba:
            if cyfra == '1':
                licznik_1 += 1
            if cyfra == '0':
                licznik_0 += 1
        if licznik_0 > licznik_1:
            zera += 1
    print(zera)

# 4.2
print('4.2')
with open('liczby.txt') as liczby:
    podzielene_2 = 0
    podzielene_8 = 0
    for liczba in liczby:
        liczba = liczba.split()[0]
        if liczba[-3:] == '000':
            podzielene_8 += 1
        if liczba[-2:] == '00':
            podzielene_2 += 1
    print(podzielene_2, podzielene_8)
print('--4.3--')
with open('liczby.txt') as liczby:
    tab_liczby = []
    for liczba in liczby:
        tab_liczby.append(liczba.split()[0])


    print(tab_liczby.index(min(tab_liczby)),min(tab_liczby))
    print(tab_liczby.index(max(tab_liczby)),max(tab_liczby))

