for i in range(1, 1000):
    num = bin(i)[2:]
    if num.count('1') % 2 == 0:
        num += '0'
        num = num.replace(num[0], '1')
        num = num.replace(num[1], '0')
    else:
        num += '1'
        num = num.replace(num[0], '1')
        num = num.replace(num[1], '1')
    r = int(num, 2)
    if r >= 16:
        print(i, r)
        break
