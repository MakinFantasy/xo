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
    if len(mas) == 2:
        print(*mas)


for i in range(338472, 338494 + 1):
    dell(i)
