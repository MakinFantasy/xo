for a in range(0, 500):
    flag = False
    for x in range(0, 500):
        for y in range(0, 500):
            if ((( x <= 9) <= (x*x <= a)) and ((y*y<=a) <= (y <= 9))) == False:
                flag = True
                break
        if flag ==  True:
            break
    if flag == False:
        print(a)

