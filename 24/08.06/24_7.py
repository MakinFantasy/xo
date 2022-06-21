f = open('3.txt')
s = f.readline()
s = s.replace('B', 'A')
s = s.replace('C', 'A')
s = s.split('A')
maxk = 0
for i in range(len(s)):
    maxk = max(len(s[i]), maxk)
print(maxk)