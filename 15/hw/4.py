for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if (((x % a != 0) and (x % 15 == 0)) <= ((x % 18 != 0) or (x % 15 != 0))) == False:
            flag = True
            break
    if flag == False:
        print(a)