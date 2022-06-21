f = open('1.txt')
s = f.readline()
print(s)
s = s.replace('B', 'A')
print(s)
s = s.split('A')
print(s)

print(len(max(s)))
