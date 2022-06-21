for n in range(200):
    r = str(bin(n)[2:])
    if n % 2 == 0:
        r += '01'
    else:
        r += '10'
    r = int(r, 2)
    if r > 130:
        print(r)
        break

