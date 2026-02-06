def pattern_count(pattern: str, text: str) -> int:
    count = 0
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            count += 1

    return count