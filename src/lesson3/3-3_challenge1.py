def frequency_table(text: str, k: int) -> dict[str, int]:
    table = {}
    n = len(text)

    for i in range(n - k + 1):
        kmer = text[i:i + k]
        if kmer in table:
            table[kmer] += 1
        else:
            table[kmer] = 1

    return table