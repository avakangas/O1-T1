while True:

    tuumat = float(input('Anna tuumamäärä: '))

    if tuumat < 0:
        print('Loppu')
        break

    senttimetrit = tuumat * 2.54
    print(f'{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.')