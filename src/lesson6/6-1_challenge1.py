import random

def weighted_die() -> int:
    r = random.random()  # value in [0, 1)

    if r < 0.1:
        return 1
    elif r < 0.2:
        return 2
    elif r < 0.7:  # 0.2 → 0.7 is 0.5 wide
        return 3
    elif r < 0.8:
        return 4
    elif r < 0.9:
        return 5
    else:
        return 6