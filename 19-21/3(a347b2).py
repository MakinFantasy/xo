from functools import lru_cache


def m(h):
    a, b = h
    return (a*2, b), (a, b*2), (a+1, b), (a, b+1)

@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 107:
        return "W"
    # if g(h*5) == "W" or g(h+1) == "W" or g(h+4) == "W":
    if any(g(x) == "W" for x in m(h)):
        return "P1"
    # if g(h*5) == "P1" and g(h+1) == "P1" and g(h+4) == "P1":
    if all(g(x) == "P1" for x in m(h)):
        return "W1"
    # if g(h*5) == "W1" or g(h+1) == "W1" or g(h+4) == "W1":
    if any(g(x) == "W1" for x in m(h)):
        return "P2"
    # if g(h * 5) == "P1" and g(h + 1) == "P2" and g(h + 4) == "P2" or \
    #     g(h*5) == "P1" and g(h+4) == "P1" or g(h+1) == "P2":
    if all(g(x) == "P1" or g(x) == "P2" for x in m(h)):
        return "W2"


for i in range(10, 100):
    h = 13, i
    print(i, g(h))
