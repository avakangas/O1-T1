pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamitta = 37.0

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. {puuttuu:.1f} cm puuttuu sallitusta pyyntimitasta.")
else:
    print("Kuha on sallittua pyyntikokoa.")
