luvut = []

while True:
    merkkijono = input('Anna luku:')
    if merkkijono == "":
        break
try:
    luku = int(merkkijono)
    luvut.append(luku)
except ValueError:
    print('Virhe')

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)