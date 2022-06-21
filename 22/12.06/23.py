def f(x):
    if x < 10:
        return x
    else:
        m = f(x // 10)
        if m < x % 10:
            return x % 10
        else:
            return m

# 6
counter = 0
for a in range(1000, 2001):
    k = 0
    for i in range(1000, a + 1):
        if f(i % 100) == 1:
            if f(i // 100) == f(i % 100):
                k += 1
    if k == 6:
        counter += 1
print(counter)
