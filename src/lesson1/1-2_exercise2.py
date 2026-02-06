def which_is_greater(x: int, y: int) -> int:
    """
    Takes two integers as inputs and returns:
    - 1 if x is greater than y
    - -1 if y is greater than x
    - 0 if they are equal
    """
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0