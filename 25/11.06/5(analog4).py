counter = 0

for i in range(10):
    s = '12347' + str(i) + '8'
    s = int(s)
    if s % 37 == 0:
        print(s, s // 37)
        counter += 1

for i in range(10):
    for j in range(10):
        s = '1234' + str(i) + '7' + str(j) + '8'
        s = int(s)
        if s % 37 == 0:
            print(s, s // 37)
            counter += 1

for i in range(10):
    for j in range(10):
        for z in range(10):
            s = '1234' + str(i) + str(j) + '7' + str(z) + '8'
            s = int(s)
            if s & 37 == 0:
                print(s, s // 37)
                counter += 1

print(counter)
