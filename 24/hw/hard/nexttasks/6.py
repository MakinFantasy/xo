with open('24-1.txt') as f:
    s = f.readline()
    print(s[0], s[1])
    counter = 1
    maxl = 0
    index = 0
    for i in range(len(s) - 1):
        if ord(s[i]) < ord(s[i+1]):
            counter += 1
        else:
            if counter > maxl:
                maxl = counter
                index = i + 1 - counter + 1
            k = 1
print(index)


f = open('24-1.txt')
s = f.readline()
print(s[0], s[1])
index = 0
maxi = 0
k = 1
for i in range(len(s) - 1):
    if ord(s[i]) < ord(s[i + 1]):
        k += 1
    else:
        if k > maxi:
            maxi = k
            index = i + 1 - k + 1
        k = 1
print(index)
