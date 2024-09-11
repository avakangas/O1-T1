vuodenajat = ('Kevät', 'Kesä', 'Syksy','Talvi')

eka = vuodenajat [0]
toka = vuodenajat [1]
kolmas = vuodenajat [2]
neljas = vuodenajat [3]

numero = int(input('Anna kuukausi (numero): '))

if numero == 12 or numero == 1 or numero == 2:
    print(f'{numero} on {neljas} kuukausi')
elif numero == 3 or numero == 4 or numero == 5:
    print(f'{numero} on {eka} kuukausi')
elif numero == 6 or numero == 7 or numero == 8:
    print(f'{numero} on {toka} kuukausi')
elif numero == 9 or numero == 10 or numero == 11:
    print(f'{numero} on {kolmas} kuukausi')