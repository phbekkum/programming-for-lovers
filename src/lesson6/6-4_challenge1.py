def count_num_digits(x: int) -> int:

    if x == 0:
        return 1

    x = abs(x)

    count = 0
    while x > 0:
        x //= 10
        count += 1

    return count