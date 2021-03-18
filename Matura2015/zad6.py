kierowcy = []
with open('Kierowcy.txt') as dane:
    for linia in dane:
        linia = linia.split(';')
        kierowcy.append(linia)
    dane.close()
wyscigi = []
with open('Wyscigi.txt') as dane:
    for linia in dane:
        linia = linia.split(';')
        wyscigi.append(linia)
    dane.close()
wyniki = []
with open('Wyniki.txt') as dane:
    for linia in dane:
        linia = linia.split(';')
        wyniki.append(linia)
    dane.close()
id_Kierowcy = 0
for rekord in kierowcy:
    if rekord[1] == 'Kubica' and rekord[2] == 'Robert':
        id_Kierowcy = rekord[0]
id_wyscigi = 0
max_punkty = 0
for rekord in wyniki:
    if rekord[0] == id_Kierowcy and int(rekord[1]) > max_punkty:
        id_wyscigi = rekord[2][:-1]
        max_punkty = int(rekord[1])
for rekord in wyscigi:
    if rekord[0] == id_wyscigi:
        sezon = rekord[1]
        nazwa = rekord[2][:-1]
with open('wyniki6.txt', 'w') as wyniki6:
    wyniki6.write('6.1 '+str(sezon)+' '+str(nazwa)+'\n')
    wyniki6.close()
print('6.1')
print(sezon, nazwa)
#Zad 6.2
tabela = []
for rekord in wyscigi[1:]:
    t = 0
    for element in tabela:
        if element[0] == rekord[2][:-1]:
            element[1] += 1
            t = 1
    if t == 0:
        tabela.append([rekord[2][:-1],1])
minimum = tabela[0]
for element in tabela:
    if element[1] < minimum[1]:
        minimum = element
print(6.2)
print(minimum[0])
with open('wyniki6.txt', 'a') as wyniki6:
    wyniki6.write('6.2 ' +str(minimum[0])+'\n')
    wyniki6.close()
sezon = ['2000', '2006', '2012']

def bierzPunkty(element):
    return element[2]
print('6.3')
klasyfikacja2012 = None
for rok in sezon:
    klasyfikacja = []
    for driver in kierowcy[1:]:
        punkty = 0
        for result in wyniki[1:]:
            if result[0] == driver[0]:
                id = result[2][:-1]
                year = None
                for race in wyscigi[1:]:
                    if race[0] == id:
                        year = race[1]
                        break
                if year == rok:
                    punkty += float(result[1].replace(',', '.'))
        klasyfikacja.append([driver[1], driver[2], punkty])
    #klasyfikacja.sort(key=bierzPunkty, reverse=True)
    klasyfikacja.sort(key=lambda x: x[2], reverse=True)
    print(rok)
    print(klasyfikacja)
    if rok == '2012':
        klasyfikacja2012 = klasyfikacja
print('6.4')
tab = []
for kierowca in klasyfikacja2012:
    if kierowca[2] > 0:
        for zawodnik in kierowcy:
            if kierowca[0] == zawodnik[1] and kierowca[1] == zawodnik[2]:
                if len(tab) > 0:
                    T = 0
                    for rekord in tab:
                        if rekord[0] == zawodnik[3][:-1]:
                            rekord[1] += 1
                            T = 1
                            break
                    if T == 0:
                        tab.append([zawodnik[3][:-1], 1])

                else:
                    tab.append([zawodnik[3][:-1], 1])
print(tab)
