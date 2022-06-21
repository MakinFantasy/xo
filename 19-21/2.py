from functools import lru_cache

def m(h):
    if h * 3 <= 83:
        return h*3, h+2
    else:
        return h + 2,


@lru_cache(None)
def g(h):
    if h > 83:
        return "L"
    if h >= 34 and h <= 83:
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


for i in range(1, 40):
    print(i, g(i))
