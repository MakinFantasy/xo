import time


start = time.time()
with open('17.txt') as f:
    s = [int(i) for i in f]
    counter = 0
    maxr = 0
    for j in range(len(s) - 1):
        if s[j+1] < s[j]:
            counter += 1
            rzn = s[j] - s[j+1]
            maxr = max(maxr, rzn)
print(counter, maxr)
print(time.time() - start)
