with open('24m_4.txt') as f:
    s = f.readline()
    s = s.replace("XZZY", "XZZ*ZZY")
    s = s.split('*')
    lmax = 0
    for i in s:
        lmax = max(lmax, len(i))
print(lmax)


# f = open('24m_4.txt')
# s = f.readline()
# s = s.replace("XZZY", "XZZ*ZZY")
# m = max(s.split('*'), key = len)


# s = open('24m_4.txt').readline()
# s = s.replace('XZZY', 'XZZ ZZY')
# m = max(s.split(), key = len)
# print(m, len(m))

