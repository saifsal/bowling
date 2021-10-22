
from random import randint


def is_strike(t: tuple) -> bool:
    return t[0] == 10


def is_spare(t: tuple) -> bool:
    return t[0] < 10 and t[0] + t[1] == 10


def play_frame() -> tuple:
    one = randint(0, 10)
    two = randint(0, 10 - one)

    assert(one + two <= 10)

    return (one, two)


def make_extra_frame(frame: tuple, extra: int) -> tuple:
    return (frame[0], frame[1], extra)


def extra_throw(frame: tuple) -> bool:
    return is_strike(frame) or is_spare(frame)


def play_game() -> list:
    game = [play_frame() for _ in range(10)]

    if extra_throw(game[-1]):
        three = randint(0, 10)
        game[-1] = make_extra_frame(game[-1], three)

    return game


def count_strikes(p: list, start: int) -> int:
    n = start
    while is_strike(p[n]) and n < 10:
        n += 1
    return n - start


def count_points(p: list) -> int:
    total = 0

    for i in range(9):
        strikes = count_strikes(p, i)

        if strikes >= 3:
            total += 30
        elif strikes == 2:
            total += 20 + sum(p[i + 2])
        elif strikes == 1:
            total += 10 + sum(p[i + 1])
        elif is_spare(p[i]):
            total += 10 + p[i + 1][0]
        else:
            total += sum(p[i])

    total += sum(p[9])

    return total


game = play_game()

print(game)

print(count_points(game))
