import time


def dell(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return n // d + d
        d += 1
    return 0


start = time.time()
counter = 0
for i in range(900000 + 1, 1_000_000):
    if dell(i) % 10 == 4:
        counter += 1
        print(i, dell(i))
    if counter == 5:
        break
print(time.time() - start)