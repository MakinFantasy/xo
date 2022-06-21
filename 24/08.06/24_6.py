f = open('3.txt')
s = f.readline()
mas = [0] * 26
for i in range(len(s) - 1):
    if s[i] == 'E':
        ind = ord(s[i+1]) - ord('A')
        mas[ind] += 1
maxe = 0
e = mas.index(max(mas))
print(mas)
print(chr(e + ord('A')))
