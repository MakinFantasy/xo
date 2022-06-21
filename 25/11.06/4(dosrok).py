for i in range(10):
    for j in range(10):
        s = 1234*10**5 + i*10**4 + 57*10**2 + j*10 + 8
        if s % 17 == 0:
            print(s, s // 17)


print('2 var') 

for i in range(10):
    for j in range(10):
        s = '1234' + str(i) + '57' + str(j) + '8'
        s = int(s)
        if s % 17 == 0:
            print(s, s//17)
