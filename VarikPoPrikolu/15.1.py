def dell(a, b):
    return a % b == 0

def logic(x, a):
    return ((not dell(x, a)) and dell(x, 6)) <= (not dell(x, 3))


for a in range(10**3, 1, -1):
    if all(logic(x, a) for x in range(1, 10**3)):
        print(a)
        break