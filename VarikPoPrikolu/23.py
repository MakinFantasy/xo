def july15(a, b):
    if a > b or a == 32:
        return 0
    elif a == b:
        return 1
    return july15(a + 3, b) + july15(a * 2, b)

print(july15(1, 16) * july15(16, 41))
