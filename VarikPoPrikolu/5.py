for n in range(1, 100):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '1' + n2 + '0'
    if n % 2 != 0:
        n2 = '11' + n2 + '11'
    n2 = int(n2, 2)
    if n2 > 52:
        print(n)
