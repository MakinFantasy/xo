for i in range(1, 1_000_000):
    x = i
    a = 0
    b = 10
    while x > 0:
        y = x % 10
        x //= 10
        if y > a:
            a = y
        if y < b:
            b = y
    if a == 5 and b == 2:
        num = str(i)
        if len(num) == 5:
            print(i)
            break

