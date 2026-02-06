import math

# Helper: cross off multiples of p
def cross_off_multiples(prime_booleans: list[bool], p: int) -> list[bool]:
    n = len(prime_booleans)
    k = 2 * p
    while k < n:
        prime_booleans[k] = False
        k += p
    return prime_booleans


# Helper: sieve of Eratosthenes
def sieve_of_eratosthenes(n: int) -> list[bool]:
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


# Main function: list all primes ≤ n
def list_primes(n: int) -> list[int]:
    """
    List all prime numbers up to and including n.
    """
    prime_booleans = sieve_of_eratosthenes(n)
    primes = [k for k in range(n + 1) if prime_booleans[k]]
    return primes