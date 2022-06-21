for a in range(0, 500):
    flag = False
    for x in range(0, 500):
        for y in range(0, 500):
            if (((y*y<=a) <= (y < 12)) and ((x < 11) <= (x*x<a))) == False:
                flag = True
                break
        if flag ==  True:
            break
    if flag == False:
        print(a)

