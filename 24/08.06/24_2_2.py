with open('2.txt') as f:
    s = f.readline()
    maxk = 0
    s = s.split('D')
    for i in s:
            maxk = max(maxk,len(i))
    print(maxk)
