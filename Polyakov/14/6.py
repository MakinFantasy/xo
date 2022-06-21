for i in range(1, 29):
    s = i
    n = 11
    while s < 224:
        s += 15
        n += 8
    if n == 115:
        print(i)
        break
