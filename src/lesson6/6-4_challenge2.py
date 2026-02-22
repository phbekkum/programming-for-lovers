def count_num_digits(x: int) -> int:
    if x == 0:
        return 1
    x = abs(x)
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

def pow10(n: int) -> int:
    return 10 ** n

def square_middle(x: int, num_digits: int) -> int:
    # Input validation
    if num_digits <= 0:
        return -1
    if num_digits % 2 == 1:
        return -1
    if x < 0:
        return -1
    if count_num_digits(x) > num_digits:
        return -1

    # Square x
    sq = x * x

    # Pad with leading zeros to length 2 * num_digits
    total_len = 2 * num_digits
    sq_str = str(sq).zfill(total_len)

    # Extract the middle num_digits digits
    start = (total_len // 2) - (num_digits // 2)
    end = start + num_digits
    middle = sq_str[start:end]

    return int(middle)