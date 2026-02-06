def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    """
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result