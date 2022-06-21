f = open('24-1.txt')
s = f.readline()
s = s.split('A')
maxd = 0
for i in range(len(s) - 1):
    kb = (s[i] + s[i+1]).count('B')
    if kb >= 3:
        maxd = max(maxd, len(s[i]) + 1 + len(s[i + 1]))
print(maxd)