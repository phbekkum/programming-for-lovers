def minimum_skew(genome: str) -> list[int]:
    skew_vals = skew_array(genome)
    min_val = min_integer_array(skew_vals)

    positions = []
    for i, v in enumerate(skew_vals):
        if v == min_val:
            positions.append(i)

    return positions