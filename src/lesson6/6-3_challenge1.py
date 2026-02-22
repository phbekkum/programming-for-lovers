def has_repeat(a: list[int]) -> bool:
    seen = set()

    for value in a:
        if value in seen:
            return True
        seen.add(value)

    return False