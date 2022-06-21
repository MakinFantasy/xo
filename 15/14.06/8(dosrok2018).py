for a in range(-200, 200):
    flag = False
    for x in range(1, 500):
        for y in range(1, 500):
            if ((y + 2*x < a) or (x > 20) or (y > 40)) == False:
                flag = True
                break
        if flag == True:
            break
    if flag == False:
        print(a)
        break
# Это можно решить ещу и руками, так что разбери это(-1:22:06)(кривой таймкод, но мне похуй)
