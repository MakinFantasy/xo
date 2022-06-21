# max m = 28(29)
# max n = 10(11)
from functools import lru_cache


# for i in range(100_000_000, 110_000_000 + 1):
#     for m in range(1, 29):
#         for n in range(11):
#             if 2**m * 7**n == i:
#                 summ = m + n
#                 print(i, summ)

# @lru_cache(None)
# def f(s):
#     for m in range(1, 28, 2):
#         for n in range(0, 11, 2):
#             if 2**m * 7**n == n:
#                 return s, m + n
#
#
# for i in range(100_000_000, 110_000_000):
#     if f(i) != None:
#         print(f(i))


for m in range(1, 29, 2):
    for n in range(0, 11, 2):
        if 100_000_000 <= 2**m * 7**n <= 300_000_000:
            print(2**m * 7**n, m+n)
