def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n/3) + 1
    if n >= 2 and n % 3 != 0:
        return f(n-2) +5


k = 0
for i in range(1, 100_000 + 1):
    if f(i) == 55:
        k += 1
print(k)
