import matplotlib.pyplot as plt

print('5.1')
kraina = []
with open('kraina.txt') as dane:
    for linia in dane:
        kraina.append([linia.split(';')[i] for i in range(0,len(linia.split(';')))])
    dane.close()
suma = [0,0,0,0]
for woj in kraina:
    region = woj[0][-1]
    if region == 'A':
        suma[0] += int(woj[1]) + int(woj[2])
    if region == 'B':
        suma[1] += int(woj[1]) + int(woj[2])
    if region == 'C':
        suma[2] += int(woj[1]) + int(woj[2])
    if region == 'D':
        suma[3] += int(woj[1]) + int(woj[2])
print(suma)
plt.bar([1,2,3,4],suma)
plt.xticks([1,2,3,4],('A','B','C','D'))
plt.xlabel('Region')
plt.ylabel('Ludność')
plt.ylim(33*10**6,58*10**6)
plt.show()

