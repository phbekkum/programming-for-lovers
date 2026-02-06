def complement(dna: str) -> str:
    comp = ""
    for base in dna:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A"
        elif base == "C":
            comp += "G"
        elif base == "G":
            comp += "C"
    return comp


def reverse(s: str) -> str:
    result = ""
    for ch in s:
        result = ch + result
    return result


def reverse_complement(dna: str) -> str:
    return reverse(complement(dna))


def starting_indices(pattern: str, text: str) -> list[int]:
    indices = []
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)
    return indices


def pattern_count(pattern: str, text: str) -> int:
    count = 0
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            count += 1
    return count


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


def find_frequent_words(text: str, k: int) -> list[str]:
    table = frequency_table(text, k)
    max_val = max_map_value(table)
    result = []
    for kmer, count in table.items():
        if count == max_val:
            result.append(kmer)
    return result


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


def skew(symbol: str) -> int:
    if len(symbol) != 1:
        raise ValueError("Input must be a single character")
    if symbol == "G" or symbol == "g":
        return 1
    if symbol == "C" or symbol == "c":
        return -1
    return 0


def skew_array(genome: str) -> list[int]:
    n = len(genome)
    array = [0] * (n + 1)
    for i in range(1, n + 1):
        array[i] = array[i - 1] + skew(genome[i - 1])
    return array


def min_integer_array(lst: list[int]) -> int:
    minimum = lst[0]
    for x in lst[1:]:
        if x < minimum:
            minimum = x
    return minimum


def minimum_skew(genome: str) -> list[int]:
    skew_vals = skew_array(genome)
    min_val = min_integer_array(skew_vals)
    positions = []
    for i, v in enumerate(skew_vals):
        if v == min_val:
            positions.append(i)
    return positions