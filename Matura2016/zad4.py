punkty = []
print('4.1')
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

print('4.2')
ilePunktow = [1000, 5000, len(punkty)]
for ile in ilePunktow:
    licznik = 0
    for punkt in punkty[:ile]:
        if (punkt[0]-200)**2 + (punkt[1]-200)**2 <= 200**2:
            licznik +=1
    print(ile)
    pi = 4*licznik/ile
    print(round(pi, 4))
