for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))) == False:
            flag = True
            break
    if flag == False:
        print(a)