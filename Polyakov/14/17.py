
maxn = 0
k = 0
with open('17.txt') as f:
    s = [int(i) for i in f]
    for i in s:
        num = hex(i)[2:]
        if num[-1] == '9':
            print(i, num)
