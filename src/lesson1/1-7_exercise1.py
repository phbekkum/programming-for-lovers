import math

def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    limit = int(math.sqrt(p))
    for d in range(3, limit + 1, 2):
        if p % d == 0:
            return False

    return True