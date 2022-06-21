import time


def dell(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return n // d - d
        d += 1
    return 0


counter = 0
start_time = time.time()
for i in range(850000 + 1, 1000000):
    if dell(i) != 0 and dell(i) % 3 == 0:
        counter += 1
        print(i, dell(i))
    if counter == 6:
        break

print(time.time() - start_time)
