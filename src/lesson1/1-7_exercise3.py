def cross_off_multiples(prime_booleans: list[bool], p: int) -> list[bool]:
    """
    Returns an updated list in which all variables whose indices are multiples
    of p (greater than p) have been set to false.
    """
    n = len(prime_booleans)

    # Start at 2p, because multiples greater than p must be crossed off
    k = 2 * p
    while k < n:
        prime_booleans[k] = False
        k += p

    return prime_booleans