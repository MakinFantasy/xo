def m(h):
    return h*5, h+4, h+1


def g(h):
    if h >= 68:
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


for i in range(5, 70):
    print(i, g(i))
