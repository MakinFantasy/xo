for i in range(12347, 10**8, 10):
    if str(i)[:4] == '1234' and i % 141 == 0:
        print(i, i // 141)