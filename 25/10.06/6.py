def f(n):
    d = 2
    mas = []
    while d * d < n:
        if n % d == 0:
            mas.append(d)
            mas.append(n // d)
        d += 1
    if d * d == n:
        mas.append(d)
    mas.sort()
    if len(mas) < 5:
        return 0
    else:
        m = mas[0] * mas[1] * mas[2] * mas[3] * mas[4]
        return m


counter = 0
for i in range(500_000_001, 550_000_000):
    m = f(i)
    if 0 < m < i:
        print(i, m)
        counter += 1
        if counter == 5:
            break

