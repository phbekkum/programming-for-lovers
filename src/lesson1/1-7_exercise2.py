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

def trivial_prime_finder(n: int) -> list[bool]:
    """
    Returns a list of boolean values storing the primality of each
    nonnegative integer up to and including n.
    """
    prime_booleans = [False] * (n + 1)

    for k in range(n + 1):
        prime_booleans[k] = is_prime(k)

    return prime_booleans