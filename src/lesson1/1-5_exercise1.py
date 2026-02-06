def min_2(a: int, b: int) -> int:
    """
    Returns the smaller of two integers.
    """
    if a < b:
        return a
    return b


def trivial_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two integers by applying a trivial algorithm
    that checks every possible divisor up to the minimum of a and b.
    """
    m = min_2(a, b)
    d = 1

    for p in range(1, m + 1):
        if a % p == 0 and b % p == 0:
            d = p

    return d