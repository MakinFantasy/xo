maxs = 0
for i in range(1, 130):
    s = '0' + '2' * i + '0'
    while '00' not in s:
        s = s.replace('02', '20', 1)
        s = s.replace('03', '30', 1)
        s = s.replace('011', '1031', 1)
        s = s.replace('01', '102', 1)
    if s.count('1') == 17 and s.count('2') == 25 and s.count('3') == 4:
        maxs = max(maxs, i)
print(maxs)
