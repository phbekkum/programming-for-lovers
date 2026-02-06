def skew_array(genome: str) -> list[int]:
    n = len(genome)
    array = [0] * (n + 1)

    for i in range(1, n + 1):
        array[i] = array[i - 1] + skew(genome[i - 1])

    return array