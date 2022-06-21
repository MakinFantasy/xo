def isprime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def find(n):
    if isprime(n):
        return False
    mas = []
    for dell in range(2, int(n**0.5) + 1):
        if n % dell == 0:
            mas.append(dell)
            mas.append(n // dell)
    if len(mas) == 2:
        if isprime(mas[0]) and isprime(mas[1]):
            r = mas[1] - mas[0]
    return r, mas[0], mas[1]


rzn = 1_000_000
for i in range(523456, 578925 + 1):
    if find(i) != False and find(i) != None:
        if find(i)[0] < rzn:
            rzn = find(i)[0]
            

