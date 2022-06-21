import time


def isprime(n):
    mas = []
    d = 1
    while d * d < n:
        if n % d == 0:
            mas.append(d)
            mas.append(n // d)
        d += 1
    if d * d == n:
        mas.append(d)
    if len(mas) == 2:
        return mas[1]


def g(n):
    counter = 0
    mas = []
    d = 2
    while d * d < n:
        if n % d == 0:
            mas.append(d)
            mas.append(n // d)
        d += 1
    if d * d == n:
        mas.append(d)
    if len(mas) > 3:
        for j in range(len(mas)):
            if isprime(mas[j]) is not None:
                counter += 1
    if counter > 3:
        return n


start = time.time()
k = 0
for i in range(2, 20000 + 1):
    if g(i) is not None:
        k += 1
        print(k, g(i))
print(time.time() - start)
