for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if (((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)) == False:
            flag = True
            break
    if flag == False:
        print(a)
        break
        