for a in range(0, 500):
    flag = False
    for x in range(0, 500):
        for y in range(0, 500):
            if ((69 != y + 2*x) or (a < x) or (a < y)) == False:
                flag = True
                break
        if flag ==  True:
            break
    if flag == False:
        print(a)

