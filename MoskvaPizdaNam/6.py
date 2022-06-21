for i in range(1000):
    s = i
    s = (s - 21) // 10
    n = 1
    while s >= 0:
        n *= 2
        s -= n
    if n == 8:
        print(i)
        break
