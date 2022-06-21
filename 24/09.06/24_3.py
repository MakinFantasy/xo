with open('24-1.txt') as f:
    s = f.readline()
    counter = 0
    s = s.replace('ABB', 'AB*BB')
    s = s.split('*')
    for i in range(len(s)):
        if len(s[i]) > counter:
            counter = len(s[i])
print(counter)
