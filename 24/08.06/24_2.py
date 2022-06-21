with open('2.txt') as f:
    s = f.readline()
    k, maxk = 0, 0
    for i in range(len(s)):
        if s[i] != 'D':
            k += 1
            maxk = max(maxk, k)
        else:
            k = 0
    print(maxk)
