for a in range(1, 1_000_000):
    flag = False
    if not((120 % a == 0) <= (not(168 % a == 0))) == False:
        flag = True
    if flag == False:
        print(a)