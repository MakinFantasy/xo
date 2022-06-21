def dell(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


k = 0
for i in range(2943444, 2943529):
    if dell(i):
        print(k, i, sep=' ', end=' ')
        k += 1
