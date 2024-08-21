luodit = float(input('Luodit:'))
naulat = float(input('Naulat:'))
leviskat = float(input('Leviskat:'))

luoti_grammana = 13.3
naula_grammana = 32 * luoti_grammana
leviskat_grammana = 20 * naula_grammana

kokonaipaino = (leviskat * leviskat_grammana) + (naulat * naula_grammana) + (luodit * luoti_grammana)

kilogrammat = int(kokonaipaino // 1000)
grammat = kokonaipaino % 1000

print(f'\nMassa on:')
print(f'{kilogrammat} Kilogrammaa sekä {grammat:.2f} grammaa')