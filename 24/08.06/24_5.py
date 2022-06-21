f = open('4.txt')
s = f.readline()
ch = 0
minch = 10**10
flag = True
for i in range(len(s)):
    if s[i] < '0' or s[i] > '9':
        flag = True
    if flag:
        if '0' <= s[i] <= '9':
            ch = ch * 10 + int(s[i])
        else:
            if ch % 2 == 0 and ch != 0:
                minch = min(minch, ch)
            ch = 0
    print(minch, ch)