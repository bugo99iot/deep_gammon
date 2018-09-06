from random import randint


def roll_dice():
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    if die_1 == die_2:
        return [die_1]*4

    return [die_1, die_2]
