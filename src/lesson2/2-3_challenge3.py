def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    """
    maximum = lst[0]

    for value in lst[1:]:
        if value > maximum:
            maximum = value

    return maximum