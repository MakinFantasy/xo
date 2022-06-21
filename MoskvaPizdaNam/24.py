with open('test.txt') as f:
    s = f.readline()
    k = 0
    maxk = 0
    gl = ['A', 'O']
    sogl = ['B', 'C', 'D']
    i = 0
    while i < len(s):
        if s[i] in gl and s[i+1] in sogl:
            k += 1
            i += 2
            maxk = max(k, maxk)
        else:
            k = 0
            i += 1
    print(maxk)
