oikea_kayttajatunnus = 'python'
oikea_salasana = 'rules'

yritykset = 0
maksimi_yritykset = 5

while yritykset < maksimi_yritykset:
    kayttajatunnus = input('Käyttäjätunnus: ')
    salasana = input('Salasana: ')

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print('Tervetuloa')
        break
    else:
        yritykset += 1
        print('Käyttäjä tai salasana väärin')

if yritykset == maksimi_yritykset:
    print('Olet yrittänyt jo liian monta kertaa')