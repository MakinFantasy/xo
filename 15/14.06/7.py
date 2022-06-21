mas = []

for a1 in range(290, 730 + 1):
    for a2 in range(a1 + 1, 730 + 1):
        flag = False
        for x in range(290, 730 + 1):
            if ((310<=x<=540) <= (((not(430<=x<=720)) and (not(a1<=x<=a2))) <= (430<=x<=720))) == False:
                flag = True
                break
        if flag == False:
            mas.append(a2-a1)
print(min(mas) / 10)

# Все числа увеличил в 10 раз, чтобы не упустить дробные части
# это первый и второй номера с 2 вебинара. Просто одинаковая прога
# 20.0 == 20
# 11.9 == 12
