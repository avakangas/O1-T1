nimi_tarkistus = {}
syötetyt_nimet = set()

while True:
    nimi = input("Syötä nimi: ").strip()

    if nimi == "":
        break

    if nimi in nimi_tarkistus:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimi_tarkistus[nimi] = True
        syötetyt_nimet.add(nimi)

print("\nSyötetyt nimet:")
for nimi in syötetyt_nimet:
    print(nimi)