counter = 0

for i in range(1, 1_000_000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 10
        x //= 10
    if a == 2 and b == 0:
        counter += 1
print(counter)
