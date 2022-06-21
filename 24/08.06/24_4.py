with open('3.txt') as f:
    k = 1
    maxk = 0
    char = str()
    s = f.readline()
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            k += 1
            if k > maxk:
                maxk = k
                ch = s[i]
        else:
            k = 1
print(ch, maxk)
