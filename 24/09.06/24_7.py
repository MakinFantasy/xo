f = open('24-174.txt')
k = 0
for s in f:
    if s.count('R') < 30:
        for i in range(len(s) - 2):
            if s[i] == s[i + 2] and s[i] != s[i + 1]:
                k += 1
print(k)
                