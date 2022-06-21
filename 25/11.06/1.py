def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


counter = 1
for i in range(4671032, 4671106 + 1):
    if isprime(i):
        print(counter, i)
        counter += 1
