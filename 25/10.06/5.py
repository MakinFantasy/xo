import time


def dell(n):
    d = 2
    mas = []
    while d * d < n:
        if n % d == 0:
            mas.append(d)
            mas.append(n // d)
        d += 1
    if d * d == n:
        mas.append(d)
    if len(mas) == 3:
        print(n, max(mas))


start = time.time()
for i in range(289123455, 389123456 + 1):
    if i**0.5 == int(i**0.5):
        dell(i)
print(time.time() - start)
