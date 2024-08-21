kanta = float(input('Anna suorakulmion kannan pituus:'))
korkeus = float(input('Anna suorakulmion korkeus:'))
pinta_ala= kanta * korkeus
piiri= 2 * (kanta + korkeus)

print(f'Suorakulmion pinat-ala on: {pinta_ala:.2f}')
print(f'Suorakulmion piiri on: {piiri:.2f}')