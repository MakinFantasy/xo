with open('17-12.txt') as f:
    s = [int(i) for i in f]
    counter = 0
    maxs = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] % 3 == 0 or s[j] % 3 == 0:
                counter += 1
                summ = s[i] + s[j]
                maxs = max(maxs, summ)

print(counter, maxs)
