def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    limit = int(x**0.5)
    for d in range(3, limit + 1, 2):
        if x % d == 0:
            return False
    return True


def next_twin_primes(n: int) -> tuple[int, int]:
    """
    Return the smallest pair of twin primes (p, p+2) such that both p and p+2 are > n.
    """
    candidate = n + 1

    while True:
        if is_prime(candidate) and is_prime(candidate + 2):
            return (candidate, candidate + 2)
        candidate += 1