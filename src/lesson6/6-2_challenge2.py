import random

def euclid_gcd(a: int, b: int) -> int:
    # Fast Euclidean algorithm using modulo
    while b != 0:
        a, b = b, a % b
    return abs(a)

def relatively_prime(a: int, b: int) -> bool:
    return euclid_gcd(a, b) == 1

def relatively_prime_probability(lower_bound: int,
                                 upper_bound: int,
                                 num_pairs: int) -> float:
    count = 0

    for _ in range(num_pairs):
        x = random.randint(lower_bound, upper_bound)
        y = random.randint(lower_bound, upper_bound)

        if relatively_prime(x, y):
            count += 1

    return count / num_pairs