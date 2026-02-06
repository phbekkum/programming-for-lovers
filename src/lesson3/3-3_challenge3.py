def find_frequent_words(text: str, k: int) -> list[str]:
    table = frequency_table(text, k)
    max_val = max_map_value(table)

    result = []
    for kmer, count in table.items():
        if count == max_val:
            result.append(kmer)

    return result