with open('17-9.txt') as f:
    s = [int(i) for i in f]
    k = 0
    maxs = 0
    for i in range(len(s) - 1):
        if s[i] % 5 == 0 and s[i+1] % 5 == 0:
            k += 1
            summ = s[i] + s[i+1]
            maxs = max(maxs, summ)
print(k, maxs)
