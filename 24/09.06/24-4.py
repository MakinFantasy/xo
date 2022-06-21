with open('24-1.txt') as f:
    s = f.readline()
    kmax = 0
    kt = 1
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            kt += 1
            kmax = max(kt, kmax)
        else:
            kt = 1
print(kmax)
