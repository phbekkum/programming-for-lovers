def factorial_array(n: int) -> list[int]:
    """
    Generates a list of factorial values from 0! to n!.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    result = [1] * (n + 1)   # initialize all entries to 1

    for k in range(1, n + 1):
        result[k] = result[k - 1] * k

    return result