n = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
print(n)
print(len(str(n)))
new_num = ''
while n > 0:
    new_num = str(n % 5) + new_num
    n //= 5
print(new_num)
print(new_num.count('0'))
