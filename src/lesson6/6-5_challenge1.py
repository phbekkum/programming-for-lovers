def generate_linear_congruence_sequence(seed: int, a: int, c: int, m: int) -> list[int]:
    sequence = []
    seen = set()

    x = seed

    while x not in seen:
        sequence.append(x)
        seen.add(x)

        x = (a * x + c) % m

    # include the repeated value
    sequence.append(x)
    return sequence