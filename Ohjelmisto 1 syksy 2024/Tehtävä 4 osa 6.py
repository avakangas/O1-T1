import random

N = 1000000
n = 0
toistot = 0

while toistot < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x ** 2 + y ** 2 < 1:
        n += 1

    toistot += 1
pii = 4 * n / N
print(pii)