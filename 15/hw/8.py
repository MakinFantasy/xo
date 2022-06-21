for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if ((x % a == 0) <= ((x % 21 == 0) + (x % 35 == 0))) == False:
            flag = True
            break
    if flag == False:
        print(a)
        break
