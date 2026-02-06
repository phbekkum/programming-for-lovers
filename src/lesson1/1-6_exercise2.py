def min_integer_array(a: list[int]) -> int:
    """
    Return the minimum integer in a non-empty list.
    """
    if not a:
        raise ValueError("List must not be empty")

    minimum = a[0]
    for value in a[1:]:
        if value < minimum:
            minimum = value

    return minimum