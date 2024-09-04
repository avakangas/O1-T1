def parittomat(luvut):
    poistetut_luvut = [luku for luku in luvut if luku % 2 == 0]
    return poistetut_luvut

lista = [7,65,3,8,2,11,4,6,7]
poistetut_luvut = parittomat(lista)
print(f'Lista aluksi: {lista}')
print(f'Parilliset luvut: {poistetut_luvut}')