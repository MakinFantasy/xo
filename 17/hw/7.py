with open('17var5.txt') as f:
    k = 0
    maxm = 0
    s = [int(i) for i in f]
    for i in range(len(s) - 1):
        if s[i] % 10 == 5 and s[i + 1] % 10 == 5:
            k += 1
            maxm = max(maxm, abs(s[i] - s[i+1]))
print(k, maxm)
