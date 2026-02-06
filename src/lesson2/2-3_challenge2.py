def divides_all(a: list[int], d: int) -> bool:
    """
    Determine whether d divides every element of a.
    """
    if d == 0:
        return False

    for x in a:
        if x % d != 0:
            return False

    return True