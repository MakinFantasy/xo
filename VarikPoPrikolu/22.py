k = 0

for i in range(1_000_000):
    x = i
    a = 0
    b = 1
    while x > 0 :
        a += 1
        b *= x % 10
        x //= 10
    if a == 2 and b == 12:
        k += 1
        print(i)
print(k)
