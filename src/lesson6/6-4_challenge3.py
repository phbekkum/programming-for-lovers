def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    sequence = []
    seen = set()

    x = seed

    while x not in seen:
        sequence.append(x)
        seen.add(x)

        x = square_middle(x, num_digits)

        # If square_middle returns -1, the sequence is invalid
        if x == -1:
            sequence.append(-1)
            return sequence

    # Include the first repeated value
    sequence.append(x)
    return sequence