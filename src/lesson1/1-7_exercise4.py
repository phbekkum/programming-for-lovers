import math

# CrossOffMultiples helper
def cross_off_multiples(prime_booleans: list[bool], p: int) -> list[bool]:
    n = len(prime_booleans)
    k = 2 * p
    while k < n:
        prime_booleans[k] = False
        k += p
    return prime_booleans


# Sieve of Eratosthenes
def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean values storing the primality of each
    nonnegative integer up to and including n, using the Sieve of Eratosthenes.
    """
    prime_booleans = [True] * (n + 1)

    if n >= 0:
        prime_booleans[0] = False
    if n >= 1:
        prime_booleans[1] = False

    limit = int(math.sqrt(n))
    for p in range(2, limit + 1):
        if prime_booleans[p]:
            cross_off_multiples(prime_booleans, p)

    return prime_booleans