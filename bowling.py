
from random import randint

SPARE = -1
MAX = 10
ROUNDS = 10


def is_strike(t: tuple) -> bool:
    return t[0] == MAX


def is_spare(t: tuple) -> bool:
    return t[0] < MAX and t[0] + t[1] == MAX


def play_frame() -> tuple:
    one = randint(0, MAX)
    two = randint(0, MAX - one)

    assert(one + two <= MAX)

    return (one, two)


def play_game() -> list:
    game = [play_frame() for _ in range(ROUNDS)]

    if is_strike(game[-1]) or is_spare(game[-1]):
        three = randint(0, MAX)
        game[-1] = (game[-1][0], game[-1][1], three)

    return game


def compute_bonuses(p: list) -> list:
    b = [0] * (len(p) - 1)
    c = 0

    for i in range(len(p) - 2, -1, -1):
        if is_strike(p[i]):
            c += 1
            b[i] = c
        elif is_spare(p[i]):
            c = 0
            b[i] = SPARE
        else:
            c = 0
            b[i] = 0

    return b


def count_points(p: list) -> int:
    total = 0
    b = compute_bonuses(p)

    for i in range(len(p) - 1):
        if b[i] >= 3:
            total += 30
        elif b[i] == 2:
            total += 20 + sum(p[i + 2])
        elif b[i] == 1:
            total += 10 + sum(p[i + 1])
        elif b[i] == SPARE:
            total += 10 + p[i + 1][0]
        else:
            total += sum(p[i])

    total += sum(p[-1])

    return total


# game = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
#        (10, 0), (10, 0), (10, 0), (10, 0, 10)]

game = play_game()

print(game)

print(count_points(game))
