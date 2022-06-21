f = open('24-s1.txt')
counter = 0
for s in f:
    for i in range(len(s) - 2):
        if s[i] == 'C' and s[i+2] == 'B':
            counter += 1
            break
print(counter)
