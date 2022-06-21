n = 6 ** 1333 - 5 * 6 ** 1215 + 3*6**144 - 86

num = ''
while n > 0:
    num = num + str(n % 6)
    n //= 6
sum = 0

for i in num:
    sum += int(i)
print(sum)
