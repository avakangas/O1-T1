import random

arpakuutio= int(input('Anna arpakuutioiden lukumäärä: '))

summa = 0

for heitto in range (arpakuutio):
    silmaluku = random.randint(1,6)
    summa = summa + silmaluku


print(summa)