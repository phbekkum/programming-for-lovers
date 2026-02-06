def min_integers(*numbers: int) -> int:
    """
    Returns the minimum value among a variable number of integers.
    """
    if len(numbers) == 0:
        raise ValueError("At least one integer must be provided")

    minimum = numbers[0]
    for value in numbers[1:]:
        if value < minimum:
            minimum = value

    return minimum