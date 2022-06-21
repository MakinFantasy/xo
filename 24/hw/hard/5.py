with open('24-j9.txt') as f:
    s = f.readline()
    a = 0
    counter = 0
    for a in range(0, len(s)):
        if s[a] == s[-a-1]:
            counter += 1

print(counter // 2)
