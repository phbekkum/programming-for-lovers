import random

def compute_craps_house_edge(num_trials: int) -> float:

    total = 0

    for _ in range(num_trials):
        if play_craps_once():
            total += 1
        else:
            total -= 1

    return total / num_trials