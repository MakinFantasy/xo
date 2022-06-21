with open('17-288.txt') as f:
    s = [int(i) for i in f]
    counter = 0
    minr = 1_000_000
    for i in range(len(s) - 2):
        if s[i] < 0 or s[i+1] < 0 or s[i+2] < 0:
            a = s[i] % 7
            b = s[i+1] % 7
            c = s[i+2] % 7
            if a != b and a != c and b != c:
                counter += 1
                rzn = max(s[i], s[i+1], s[i+2]) - min(s[i], s[i+1], s[i+2])
                minr = min(minr, rzn)
print(counter, minr)
