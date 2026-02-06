def sum_integers(*numbers: int) -> int:
    """
    Return the sum of a variable number of integers.
    """
    total = 0
    for value in numbers:
        total += value
    return total