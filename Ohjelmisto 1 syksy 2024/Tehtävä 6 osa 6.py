import math

def lakse(halkaisija, hinta):
    sade = halkaisija / 2
    pintaala = math.pi * (sade ** 2) / 1000
    yksikko = hinta / pintaala
    return yksikko

halkaisija1 = float(input('Anna ensimmäisen pitsan halkaisija: '))
hinta1 = float(input('Anna ensimmäisen pitsan hinta: '))

halkaisija2 = float(input('Anna toisen pitsan halkaisija:'))
hinta2 = float(input('Anna toisen pitsan hinta:'))

yksilohinta1 = laske_yksilohinta(halkaisija1, hinta1)
yksilohinta2 = laske_yksilohinta(halkaisija2, hinta2)

print(f'Ensimmäisen pitsan hinta: {ysikohinta1:2f} euro/neliömetri')
print(f'Toisen pitsan hinta: {yksilohinta2:2f}euroa/neliömetri')

if yksilohinta1 < yksilohinta2:
    print('Ensimmäinen pitsa antaa paremman vastineen rahalle.')
elif yksilohinta2 < yksilohinta1:
    print('Toinen pitsa antaa paremman vastineen rahalle.')
else:
    print('Molemmat pitsat ovat hyvä vastine rahalle.')