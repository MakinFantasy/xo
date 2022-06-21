with open('k7c-6.txt') as f:
    s = f.readline()
    counter = 0
    for i in range(len(s) - 2):
        if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
            counter += 1
print(counter)