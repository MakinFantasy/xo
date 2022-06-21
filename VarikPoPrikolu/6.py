for i in range(1_000):
    s = i
    n = 0
    while s + n < 450:
        s -= 5
        n += 25
    if n == 50:
        print(i, n)

for i in range(1_000_000):
    s = i
    n = 0
    while 400 < s*s:
        s -= 1
        n += 3
    if n <= 1000:
        print(i)