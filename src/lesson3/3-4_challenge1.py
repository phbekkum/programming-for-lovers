def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    patterns = []
    n = len(text)

    for i in range(n - window_length + 1):
        window = text[i:i + window_length]
        freq_map = frequency_table(window, k)

        for s, count in freq_map.items():
            if count >= t and s not in patterns:
                patterns.append(s)

    return patterns