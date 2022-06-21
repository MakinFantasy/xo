mina = 10000
with open('24-s1.txt') as user_file:
    for line in user_file:
        if line.count('A') < mina:
            mina = line.count('A')
            st = line
    mas = [0] * 26
    for i in range(len(st) - 1):
        ind = ord(st[i]) - ord('A')
        mas[ind] += 1

    maxk = 0
    for i in range(len(mas)):
        if mas[i] >= maxk:
            maxk = mas[i]
            e = i

    buk = chr(e + ord('A'))
with open('24-s1.txt') as user_file:
    res = 0
    for s in user_file:
        res += s.count(buk)

    print(buk,res)  