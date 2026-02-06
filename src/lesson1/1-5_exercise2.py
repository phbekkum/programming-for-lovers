def euclid_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two integers by applying Euclid's algorithm.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a