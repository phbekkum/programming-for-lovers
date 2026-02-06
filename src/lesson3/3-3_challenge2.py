def max_map_value(dictionary: dict[str, int]) -> int:
    first = True
    maximum = 0

    for value in dictionary.values():
        if first:
            maximum = value
            first = False
        elif value > maximum:
            maximum = value

    return maximum