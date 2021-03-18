import math
import matplotlib.pyplot as plt

punkty = []
print('---4.1---')
with open('punkty.txt') as file:
    for linia in file:
        punkty.append([int(linia.split()[0]),int(linia.split()[1])])
    file.close()
licznik = 0
for punkt in punkty:
    if (punkt[0]-200)**2 + (punkt[1]-200)**2 == 200**2:
        print(punkt)
    elif (punkt[0]-200)**2 + (punkt[1]-200)**2 < 200**2:
        licznik +=1
print(licznik)

print('---4.2---')
ilePunktow = [100, 1000, 5000, len(punkty)]
for ile in ilePunktow:
    licznik = 0
    for punkt in punkty[:ile]:
        if (punkt[0]-200)**2 + (punkt[1]-200)**2 <= 200**2:
            licznik +=1
    print('n =', ile)
    pi = 4*licznik/ile
    print('pi =', round(pi, 4), '\n')
print('---4.3---')
eps_tab = []
for ile in range(1, 1701, 1):
    licznik = 0
    pi = 0
    for punkt in punkty[:ile]:
        if (punkt[0]-200)**2 + (punkt[1]-200)**2 <= 200**2:
            licznik +=1
    pi = 4*licznik/ile
    eps = math.fabs(math.pi - pi)
    eps_tab.append(eps)
plt.plot(eps_tab)
plt.ylabel('epsilon')
plt.xlabel('n')
plt.ylim([-0.1, 1])
plt.xlim([-10, 1710])
plt.grid(color = 'r', linestyle = '--', linewidth = 1)
plt.show()
with open('wyniki_4.txt', 'w') as file:
    file.write(str(round(eps_tab[999], 4)) + '\n')
    file.write(str(round(eps_tab[-1], 4)) + '\n')
