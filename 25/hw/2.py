import time


def isprime(n):
    for dell in range(2, int(n**0.5)+1):
        if n % dell == 0:
            return False
    return True


def f(n):
    mas = []
    k = 0
    if isprime(n):
        return False
    for dell in range(2, int(n**0.5) + 1):
        if n % dell == 0:
            mas.append(dell)
            mas.append(n // dell)
    for d in mas:
        if isprime(d):
            k += 1
    if k > 3:
        return True
    return False


start = time.time()
counter = 0
for i in range(2, 20001):
    if f(i):
        counter += 1
        print(i, counter)
print(f"Answer is {counter}")
print(time.time() - start)
