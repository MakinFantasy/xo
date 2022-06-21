s = '02460'
s1 = '04260'
s2 = '02466420'
s3 = '02466240'
while '00' not in s:
    s = s.replace('02', '6404', 1)
    s = s.replace('04', '2206', 1)
    s = s.replace('06', '440', 1)
print(s)
while '00' not in s1:
    s1 = s1.replace('02', '6404', 1)
    s1 = s1.replace('04', '2206', 1)
    s1 = s1.replace('06', '440', 1)
print(s1)
while '00' not in s2:
    s2 = s2.replace('02', '6404', 1)
    s2 = s2.replace('04', '2206', 1)
    s2 = s2.replace('06', '440', 1)
print(s2)
while '00' not in s3:
    s3 = s3.replace('02', '6404', 1)
    s3 = s3.replace('04', '2206', 1)
    s3 = s3.replace('06', '440', 1)
print(s3)

for i in range(1, 10**2):
    for z in range(1, 10**2):
        for j in range(1, 10**2):
            s = '0' + '2' * i + '4' * j + '6' * z + '0'
            s1 = '0' + '2' * i + '4' * j + '6' * z + '0'
            while '00' not in s:
                s = s.replace('02', '6404', 1)
                s = s.replace('04', '2206', 1)
                s = s.replace('06', '440', 1)

            if s.count('2') == 30 and s.count('4') == 54 and s.count('6') == 10:
                print(s1.count('6'))
