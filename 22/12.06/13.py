for i in range(1, 1_000_000):
    x = i
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 == 0:
            m += x % 10
        x //= 10
    if l == 3 and m == 0:
        print(i)
        