def dell(n):
    dells = []
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            dells.append(i)
            dells.append(n // i)
    if len(dells) == 2:
        return dells
    return None


for i in range(174457, 174506):
    result = dell(i)
    if result is not None:
        print(*result, sep=' ', end=' ')

