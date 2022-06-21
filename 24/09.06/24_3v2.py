with open('24-1.txt') as f:
    s = f.readline()
    kmax = 0
    kt = 0
    for i in range(len(s) - 2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'B':
            kt += 2
            kmax = max(kt, kmax)
            kt = 0
        else:
            kt += 1
kt += 2 # В конце файла не может быть комбинация ABB, поэтому добавляем +2
kmax = max(kt, kmax)
print(kmax)
