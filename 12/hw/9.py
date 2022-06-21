s = '23' * 30 + '1' * 30
while '21' in s or '23' in s:
        s = s.replace('21', '11', 1)
        s = s.replace('23', '21', 1)
print(s)
print(s.count('1'))
