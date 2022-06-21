with open('24-j6.txt') as f:
    s = f.readline()
    kt = 1
    res = 0
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            kt += 1
        else:
            if kt == 7:
                res += 1
            kt = 1
    if kt == 7:
        res += 1
print(res)
