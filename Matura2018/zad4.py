dane = []
with open('sygnaly.txt', 'r') as file:
    for line in file:
        dane.append(line[:-1])
print('---4.1---')
slowo = ""
for i in range(39, len(dane), 40):
    slowo += dane[i][9]
with open('wyniki4.txt', 'w') as file:
    file.write(slowo)
