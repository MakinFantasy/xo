with open('24.txt') as f:
    s = f.readline()
    k = 0
    maxl = 0
    m = 0
    for i in range(len(s)):
        k += 1
        if s[i] == 'Z':
            m += 1
        if m == 2:
            k = k - 1
            m = 1
            maxl = max(k, maxl)
            k = 1
print(maxl)


f = open('24m_4.txt').readline()
k = 0
maxk = 0
m = 0
for i in range(len(f)):
    k+=1
    if f[i] == 'Z':
        m+=1
    if m == 2:
        k = k - 1
        m = 1
        maxk = max(k, maxk)
        k = 1
    #print (k , f[i])  <-- это для проверки
print(maxk)