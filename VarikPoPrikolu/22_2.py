for i in range(1_000_000):
    x = i
    x0 = x
    n = 0
    while x > 0:
        d = x % 3
        n = n*10 + d
        x //= 3
    n += x0
    num = str(n)
    if len(num) == 4:
        print(i)
        print(num)
        break

x = 10
x0 = x # 27
n = 0
while x > 0:
    d = x % 3
    n = n*10 + d
    x //= 3
n += x0
print(n)
