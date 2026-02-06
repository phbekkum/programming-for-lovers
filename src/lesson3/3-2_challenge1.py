def starting_indices(pattern: str, text: str) -> list[int]:
    indices = []
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)

    return indices