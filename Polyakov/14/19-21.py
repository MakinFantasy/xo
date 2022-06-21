from functools import lru_cache


def game(h):
    return h+2, h+3, h*2

@lru_cache(None)
def f(h):
    if h >= 30:
        return 'W'
    elif any(f(x) == 'W' for x in game(h)):
        return 'P1'
    elif any(f(x) == 'P1' for x in game(h)):
        return 'V1'
    elif any(f(x) == 'V1' for x in game(h)):
        return 'P2'
    elif all(f(x) == 'P2' for x in game(h)):
        return 'V2'


for i in range(1, 30):
    print(i, f(i))
