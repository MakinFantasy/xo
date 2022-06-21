import time


def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def sprime(n):
    s = 0
    d = 2
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                s += d
            if isprime(n // d):
                s += n // d
        d += 1
    if d * d == n:
        if isprime(d):
            s += d
    return s


start = time.time()
counter = 0
for i in range(550_001, 600_000):
    if sprime(i) % 10 == 1:
        s = sprime(i)
        print(i, s)
        counter += 1
    if counter == 5:
        break
print(time.time() - start)

