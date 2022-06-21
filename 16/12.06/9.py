def f(n):
    global counter
    counter += 1
    if n >= 1:
        counter += 1
        f(n-1)
        f(n-2)
        counter += 1


counter = 0
f(35)
print(counter)
