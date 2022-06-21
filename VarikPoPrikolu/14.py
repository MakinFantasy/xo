num = 9**11*3**20-3**9-27
new_num = str()
while num > 0:
    new_num += str(num % 3)
    num //= 3
print(new_num.count('2'))
