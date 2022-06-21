import time


def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def maxd(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            if not(isprime(n // d)):
                return n // d
        d += 1
    return 0


counter = 0
for i in range(450_001, 500_000):
    if maxd(i) != 0:
        m = maxd(i)
        print(i, m)
        counter += 1
    if counter == 6:
        break
