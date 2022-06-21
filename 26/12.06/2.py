# 55

with open('26A7.txt') as f:
    s = [int(i) for i in f]
    minimal = min(s)
    counter = 0
    for j in s:
        if j < 55:
            counter += 1
print(minimal, counter)
    