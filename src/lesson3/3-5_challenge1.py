def skew(symbol: str) -> int:
    if len(symbol) != 1:
        raise ValueError("Input must be a single character")

    if symbol == 'G' or symbol == 'g':
        return 1
    if symbol == 'C' or symbol == 'c':
        return -1
    return 0