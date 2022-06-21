with open('27_B.txt') as f:
    s = [int(i) for i in f]
    s.sort()
    for i in range(101):
        print(s[i])

