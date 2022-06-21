# Код говна, но мне похуй

with open('k7c-3.txt') as f:
    s = f.readline()
    counter = 0
    mas = []
    for i in range(len(s) - 4):
        mas.append(s[i])
        mas.append(s[i+1])
        mas.append(s[i+2])
        mas.append(s[i+3])
        mas.append(s[i+4])
        if mas[0] != mas[1]:
            if mas[1] != mas[2]:
                if mas[2] != mas[3]:
                    if mas[3] != mas[4]:
                        counter += 1
        mas.clear()
print(counter)
