with open('24-s1.txt') as f:
    s = f.readlines()
    counter = 0
    for i in s:
        if i.count('YZ') > 1:
            counter += 1
print(counter)
