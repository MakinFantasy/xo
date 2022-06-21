counter = 0


for j in range(10, 100):
    n = j
    i = 0
    while n > 0:
        i += n % 8
        n //= 8
    if i % 7 == 0:
        print(j)
        counter += 1
print('----------')
print(counter)
