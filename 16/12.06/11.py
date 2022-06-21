def f(n):
    global s
    s += n + 1
    if n > 1:
        s += 2 * n
        f(n-1)
        f(n-3)


for i in range(1, 1000):
    s = 0
    f(i)
    if s > 10 ** 6:
        print(i, s)
        break
