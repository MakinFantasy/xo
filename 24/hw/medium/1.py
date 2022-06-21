with open("24_4.txt") as f:
    s = f.readline()
    counter = 0
    maxl = 0
    for i in range(len(s) - 1):
        if s[i] == 'Q' and s[i+1] == 'Q':
            counter = 1
        else:
            counter += 1
            if maxl < counter:
                maxl = counter
print(counter, maxl)
