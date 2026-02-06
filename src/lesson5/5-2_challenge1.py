import random

def play_craps_once() -> bool:

    # First roll (come-out roll)
    first = sum_dice(2)

    # Immediate win
    if first == 7 or first == 11:
        return True

    # Immediate loss
    if first in (2, 3, 12):
        return False

    # Otherwise, enter the point phase
    point = first

    while True:
        roll = sum_dice(2)

        if roll == point:
            return True
        if roll == 7:
            return False