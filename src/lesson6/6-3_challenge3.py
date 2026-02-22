import random

def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    count_shared = 0

    for _ in range(num_trials):
        if simulate_one_birthday_trial(num_people):
            count_shared += 1

    return count_shared / num_trials