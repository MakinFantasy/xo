with open('17.txt') as f:
    k = 0
    summ = 0
    kol = 0
    s = [int(i) for i in f]
    for i in range(len(s)):
        if s[i] % 2 != 0:
            summ += s[i]
            kol += 1
    avg = summ / kol
    summary = 0
    maxs = 0
    for i in range(len(s) - 2):
        a = s[i] % 3
        b = s[i+1] % 3
        c = s[i+2] % 3
        if a != b and a != c and b != c:
            if (s[i] < avg and s[i + 1] >= avg and s[i + 2] >= avg) or (s[i] >= avg and s[i + 1] < avg and s[i + 2] >= avg) or (s[i] >= avg and s[i + 1] >= avg and s[i + 2] < avg):
                k += 1
                summary = s[i] + s[i+1] + s[i+2]
                maxs = max(maxs, summary)
print(k, maxs)
