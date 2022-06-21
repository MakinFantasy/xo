print("Два самых имбовых способов решения подобных номеров")

print("I варик")

from collections import Counter
f = open('24-s2.txt')
s = f.readline()
a = ''
for i in range(len(s) - 2):
    if s[i] == 'A' and s[i+2] == 'C':
        a+=s[i+1]
print(Counter(a).most_common())

print("II варик")

f = open('24-s2.txt')
s = f.readline()
a = ''
for i in range(len(s) - 2):
    if s[i] == 'A' and s[i+2] == 'C':
        a += s[i+1]
bukva = max(a, key=a.count)
print(bukva + str(a.count(bukva)))
