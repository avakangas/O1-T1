def gallona_l(gallona):
    return gallona * 3,785
while True:
    gallona = float(input('Anna bensiinin määrä:'))

if gallona < 0:
    print('virhe')
    breakpoint

litra = gallona_l(gallona)
print(f'{gallonat} gallonaa on {litra}litraa')

