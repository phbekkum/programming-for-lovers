def max_integers(*numbers: int) -> int:
    """
    Return the maximum integer among a variable number of inputs.
    """
    if len(numbers) == 0:
        raise ValueError("At least one integer must be provided")

    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value

    return maximum