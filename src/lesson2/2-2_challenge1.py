def power(a: int, b: int) -> int:
    """
    Compute a raised to the b-th power.
    """
    result = 1
    for _ in range(b):
        result *= a
    return result