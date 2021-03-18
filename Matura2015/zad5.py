import matplotlib.pyplot as plt
import math

print('5.1')
kraina = []
with open('kraina.txt') as dane:
    for linia in dane:
        kraina.append([linia.split(';')[i] for i in range(0,len(linia.split(';')))])
    dane.close()
suma = [0,0,0,0]
licznik = [0,0,0,0]
for woj in kraina:
    region = woj[0][-1]
    if region == 'A':
        suma[0] += int(woj[1]) + int(woj[2])
        if woj[1] < woj[3] and woj[2] < woj[4]:
            licznik[0] += 1
    if region == 'B':
        suma[1] += int(woj[1]) + int(woj[2])
        if woj[1] < woj[3] and woj[2] < woj[4]:
            licznik[1] += 1
    if region == 'C':
        suma[2] += int(woj[1]) + int(woj[2])
        if woj[1] < woj[3] and woj[2] < woj[4]:
            licznik[2] += 1
    if region == 'D':
        suma[3] += int(woj[1]) + int(woj[2])
        if woj[1] < woj[3] and woj[2] < woj[4]:
            licznik[3] += 1
print(suma)
plt.bar([1,2,3,4],suma)
plt.xticks([1,2,3,4],('A','B','C','D'))
plt.xlabel('Region')
plt.ylabel('Ludność')
plt.ylim(33*10**6,58*10**6)
#plt.show()

print('5.2')
#print(licznik, sum(licznik))
print('Kraj: ', sum(licznik), ' \nA:', licznik[0], 'B:', licznik[1], 'C:', licznik[2], 'D:', licznik[3])
#print('Kraj: %d \nA: %d' % (sum(licznik), licznik[0]))

print('5.3')
#ludnosc do roku 2025
rok = 2025
rok_p = 2013
ludnosc_t = []
licznik_p = 0
for woj in kraina:
    tempo = int(10000 * ((int(woj[3]) + int(woj[4]))/(int(woj[1]) + int(woj[2])))) / 10000
    ludnosc = int(woj[3]) + int(woj[4])
    for _ in range(rok_p + 2, rok + 1, 1):
        ludnosc = int(ludnosc * tempo)
        if ludnosc > 2 * (int(woj[1]) + int(woj[2])):
            licznik_p += 1
            break
    ludnosc_t.append([woj[0], ludnosc, tempo])
ludnosc = 0
maksimum = ludnosc_t[0]
for rekord in ludnosc_t:
    ludnosc += rekord[1]
    if rekord[1] > maksimum[1]:
        maksimum = rekord

print(maksimum[0])
print(ludnosc)
print(licznik_p)
file = open('Wynik2.txt','w')
file.write(str(maksimum[0]))
file.close()
#sprawdzic, gdzie jest najw ludnosc i zsumowac


