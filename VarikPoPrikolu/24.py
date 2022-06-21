import collections

with open('24m_5.txt') as f:
    s = f.readline()
    m = ''
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            m += s[i+1]

print(collections.Counter(m))

