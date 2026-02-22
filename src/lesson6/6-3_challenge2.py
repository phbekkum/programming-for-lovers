import random

def has_repeat(a: list[int]) -> bool:
    seen = set()
    for x in a:
        if x in seen:
            return True
        seen.add(x)
    return False

def simulate_one_birthday_trial(num_people: int) -> bool:
    birthdays = []

    for _ in range(num_people):
        # Random birthday between 1 and 365
        day = random.randint(1, 365)
        birthdays.append(day)

    return has_repeat(birthdays)