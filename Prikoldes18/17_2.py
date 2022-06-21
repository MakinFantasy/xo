import time

with open('17_2.txt') as f:
    s = [int(i) for i in f]
    avg = 0
    num_k = 0
    summ = 0
    counter = 0
    for i in range(len(s)):
        if s[i] % 2 == 0:
            num_k += 1
            summ += s[i]
    avg = summ / num_k
    for i in range(len(s) - 1):
        if s[i] % 3 == 0 or s[i+1] % 3 == 0:
            if s[i] < avg or s[i+1] < avg:
                counter += 1
print(counter)
