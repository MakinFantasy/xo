alf = '01234567'
k = 0
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                for s5 in alf:
                    s = s1+s2+s3+s4+s5
                    if s.count('6') == 1 and s[0] != '0':
                        if '61' not in s and '63' not in s and '65' not in s and '67' not in s:
                            if '16' not in s and '36' not in s and '56' not in s and '76' not in s:
                                k += 1
print(k)
