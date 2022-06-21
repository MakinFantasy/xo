def f(n):
    return n*n*n

def g(n):
    return n*n


for j in range(1, 1_000_000):
    k = j
    i = 1
    while f(i) < k *g(i):
        i += 1
    if i == 15:
        print(j)
        break
