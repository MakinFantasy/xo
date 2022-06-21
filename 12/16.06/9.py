s = '23' * 30 + '1' * 30
mas = []
while '21' in s or '23' in s:
    if '21' in s:
        s = s.replace('21', '11', 1)
    else:
        s = s.replace('23', '21', 1)
    mas.append(s)


maxl = 0
for i in range(len(mas)):
    if mas[i].count('1') > maxl:
        maxl = mas[i].count('1')
print(maxl)

# преобразовываем s так, чтобы получить максимальное кол-во