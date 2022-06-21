with open('17-6.txt') as f:
    s = [int(i) for i in f]
    maxs = 0
    k = 0
    for i in range(len(s) - 2):
        a = bin(s[i])[2:].count('1')
        b = bin(s[i+1])[2:].count('1')
        c = bin(s[i+2])[2:].count('1')
        if a == 2 and b == 2 and c == 2:
            k += 1
            summ = s[i] + s[i+1] + s[i+2]
            maxs = max(maxs, summ)
print(k, maxs)


# with open ('17-6.txt') as f:
#     s=[int(i) for i in f]
#     k=0
#     maxs=0
#     for i in range(len(s)-2):
#         a=bin(s[i])
#         b=bin(s[i+1])
#         c=bin(s[i+2])
#         if a.count('1')==2 and b.count('1')==2 and c.count('1')==2 :
#             k+=1
#             maxs=max(maxs,s[i]+s[i+1]+s[i+2])
#     print(k,maxs)