# 2 max 29(28)
# 3 max 18(17)


mas = []

for m in range(0, 29, 2):
    for n in range(1, 18, 2):
        x = 2**m * 3**n
        if 150_000_000 <= x <= 300_000_000:
            mas.append(x)

mas.sort()
counter = 1
for i in mas:
    print(counter, i)
    counter += 1
