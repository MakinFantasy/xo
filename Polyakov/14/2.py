print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not (((x <= y) or (not (z <= w))) and ((w <= (not x)) or ((not y) <= z))):
                    print(x, y, w, z)
