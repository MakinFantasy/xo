# 178 min height
# 100 summary

with open('26_11.txt') as f:
    s = [int(i) for i in f]
    minimal = min(s)
    maximal = max(s)
    counter = 0
    for j in s:
        if j >= 178:
            counter += 1
print(counter, maximal - minimal)
        