for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if ((x % a != 0) <= ((x % 54 == 0) <= (162 % x != 0))) == False:
        # if ((x % a != 0) <= ((x % 54 == 0) <= (162 % x != 0))) == False:
            flag = True
            break
    if flag == False:
        print(a)