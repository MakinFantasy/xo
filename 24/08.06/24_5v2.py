f = open('4.txt')
s = f.readline()
for i in s:
    if not(i.isdigit()):
        s = s.replace(i, '*')
s = s.split('*')
print(s)
# minch = 10 ** 10
# for i in range(1, len(s) - 1):
#     ch = int(s[i])
#     if ch != 0 and ch % 2 == 0:
#         minch = min(minch, ch)
# print(minch)


### Доделать
