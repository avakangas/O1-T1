lentoasemat = {}

while True:
    valinta = input(
        "Valitse toiminto:\n"
        "1. Syötä uusi lentoasema\n"
        "2. Hae lentoaseman tiedot\n"
        "3. Lopeta\n"
        "Syötä valintasi (1/2/3): ").strip()

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
        nimi = input("Syötä lentoaseman nimi: ").strip()

        lentoasemat[icao_koodi] = nimi
        print(f"Lentoasema {nimi} (ICAO-koodi: {icao_koodi}) on lisätty.")

    elif valinta == "2":
        icao_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ").strip().upper()

        if icao_koodi in lentoasemat:
            print(f"Lentoaseman nimi ICAO-koodilla {icao_koodi} on {lentoasemat[icao_koodi]}.")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao_koodi} ei löydy.")

    elif valinta == "3":
        print("Virhe, loppu.")
        break

    else:
        print("Virheellinen valinta.")