from itertools import product
counter = 0
for r in range(3):
    for i in product('0123456789', repeat=r):
        x = "".join(i)
        for z in range(10):
            s = '1234' + x + '7' + str(z) + '8'
            s = int(s)
            if s % 37 == 0:
                print(s, s//37)
                counter += 1
print(counter)