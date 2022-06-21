for j in range(100):
    n = j
    i = 0
    while n > 0:
        i += n % 16
        n //= 16
    if i % 15 == 0:
        print(j)
        