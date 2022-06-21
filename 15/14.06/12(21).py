for a in range(0, 100):
    flag = False
    for x in range(0, 100):
        if ((x&a != 0) <= ((x&12 == 0) <= (x&5!=0))) == False:
            flag = True
    if flag == False:
        print(a)