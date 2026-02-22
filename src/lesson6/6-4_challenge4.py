def compute_period_length(a: list[int]) -> int:
    first_index = {}

    for i, value in enumerate(a):
        if value in first_index:
            # period = distance between first and second occurrence
            return i - first_index[value]
        first_index[value] = i

    return 0