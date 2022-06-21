with open('24.txt') as f:
    s = f.readlines()
    maxl = 0
    for string in s:
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                if string[i] == string[j]:
                    rzn = j - i
                    maxl = max(maxl, rzn)
print(maxl)
