import random

def heitto(maara):
    return random.randint(1,maara)

maara = int(input('Anna määrä:'))

luku = 0

while luku != maara:
    luku = heitto(maara)
    print(f'Tulos on : {luku}')