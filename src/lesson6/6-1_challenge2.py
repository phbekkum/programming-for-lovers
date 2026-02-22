import random

def estimate_pi(num_points: int) -> float:
    count_inside = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y <= 1:
            count_inside += 1

    return 4 * (count_inside / num_points)