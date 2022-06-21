for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        if ((((x % 36 == 0) and (x % 42 == 0)) <= (x % a == 0)) and (a*(a - 25) < 25 * (a + 200))) == False:
            flag = True
            break
    if flag == False:
        print(a)