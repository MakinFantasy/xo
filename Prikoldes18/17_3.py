import time

maxdel = 0
mins = 1_000_000_000
k = 0

with open('17-243.txt') as f:
    s = [int(i) for i in f]
    for i in s:
        if i % 171 == 0:
            maxdel = max(maxdel, i)

    for i in range(len(s) - 1):
        if s[i] < maxdel or s[i+1] < maxdel:
            if '11' in str(s[i]) or '11' in str(s[i + 1]):
                k += 1
                summ = s[i] + s[i+1]
                mins = min(mins, summ)
print(k, mins)
