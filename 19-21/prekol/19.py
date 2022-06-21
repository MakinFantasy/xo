from functools import lru_cache


def moves(h):
    a, b, c = h
    return (a + 23, b, c), (a, b + 23, c), (a, b, c + 23), (a + 13, b, c), (a, b + 13, c), (a, b, c + 13), (a + 3, b, c), (a, b + 3, c), (a, b, c + 3)


@lru_cache(None)
def game(h):
    if sum(h) >= 73:
        return 'W'
    if any(game(x) == 'W' for x in moves(h)):
        return 'P1'
    if any(game(x) == 'P1' for x in moves(h)):
        return 'V1'


for i in range(1, 24):
    h = (2, i, i * 2)
    print(i, game(h))
    