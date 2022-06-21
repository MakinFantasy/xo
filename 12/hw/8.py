for a in range(50):
    for b in range(50):
        for c in range(50):
            s = '0' + '1' * a + '2' * b + '3' * c + '0'
            while '00' not in s:
                s = s.replace('01', '210')
                s = s.replace('02', '3101')
                s = s.replace('03', '2012')
            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(a + b + c + 2)
