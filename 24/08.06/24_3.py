with open('3.txt') as f:
    s = f.readline()
    k = 1
    maxk = 0
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            k += 1
            maxk = max(maxk, k)
        else:
            k = 1
print(maxk)
