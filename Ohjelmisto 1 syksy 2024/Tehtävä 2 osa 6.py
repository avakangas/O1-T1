import random

kolmenumeroinenkoodi = ''
for _ in range (3):
    kolmenumeroinenkoodi += str(random.randint(0,9))

nelinumeroinenkoodi = ''
for _ in range (4):
    nelinumeroinenkoodi += str(random.randint(1,6))

print(f'Kolminumeroinen koodi: {kolmenumeroinenkoodi}')
print(f'Nelinumeroinen koodi: {nelinumeroinenkoodi}')