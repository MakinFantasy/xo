import math
import time


def divisorgenerator(n):
    large_divisors = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


start = time.time()
for i in range(289123456, 398123456 + 1):
    div = list(divisorgenerator(i))
    if len(div) == 3:
        print(div)
        print(i, max(div))
print(time.time() - start)
