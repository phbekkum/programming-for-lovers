import random

def weighted_die() -> int:
    r = random.random()
    if r < 0.1:
        return 1
    elif r < 0.2:
        return 2
    elif r < 0.7:
        return 3
    elif r < 0.8:
        return 4
    elif r < 0.9:
        return 5
    else:
        return 6

def estimate_pi(num_points: int) -> float:
    inside = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / num_points

def euclid_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)

def relatively_prime(a: int, b: int) -> bool:
    return euclid_gcd(a, b) == 1

def relatively_prime_probability(lower_bound: int, upper_bound: int, num_pairs: int) -> float:
    count = 0
    for _ in range(num_pairs):
        x = random.randint(lower_bound, upper_bound)
        y = random.randint(lower_bound, upper_bound)
        if relatively_prime(x, y):
            count += 1
    return count / num_pairs

def has_repeat(a: list[int]) -> bool:
    seen = set()
    for x in a:
        if x in seen:
            return True
        seen.add(x)
    return False

def simulate_one_birthday_trial(num_people: int) -> bool:
    birthdays = [random.randint(1, 365) for _ in range(num_people)]
    return has_repeat(birthdays)

def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    count = 0
    for _ in range(num_trials):
        if simulate_one_birthday_trial(num_people):
            count += 1
    return count / num_trials

def count_num_digits(x: int) -> int:
    if x == 0:
        return 1
    x = abs(x)
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

def square_middle(x: int, num_digits: int) -> int:
    if num_digits <= 0 or num_digits % 2 == 1:
        return -1
    if x < 0:
        return -1
    if count_num_digits(x) > num_digits:
        return -1

    sq = x * x
    total_len = 2 * num_digits
    sq_str = str(sq).zfill(total_len)

    start = (total_len // 2) - (num_digits // 2)
    end = start + num_digits

    return int(sq_str[start:end])

def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    sequence = []
    seen = set()
    x = seed

    while x not in seen:
        sequence.append(x)
        seen.add(x)
        x = square_middle(x, num_digits)
        if x == -1:
            sequence.append(-1)
            return sequence

    sequence.append(x)
    return sequence

def compute_period_length(a: list[int]) -> int:
    first_index = {}
    for i, value in enumerate(a):
        if value in first_index:
            return i - first_index[value]
        first_index[value] = i
    return 0

def generate_linear_congruence_sequence(seed: int, a: int, c: int, m: int) -> list[int]:
    sequence = []
    seen = set()
    x = seed

    while x not in seen:
        sequence.append(x)
        seen.add(x)
        x = (a * x + c) % m

    sequence.append(x)
    return sequence