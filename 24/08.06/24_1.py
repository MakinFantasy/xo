f = open('1.txt')
s = f.readline()
k = 0
maxk = 0
for i in range(len(s)):
    if s[i] == 'C':
        k += 1
        maxk = max(maxk, k)
    else:
        k = 0
print(maxk)
