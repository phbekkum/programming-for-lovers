import math
import random

def sum_dice(num_dice: int) -> int:

    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total