import random

def add_noise(polling_value: float, margin_of_error: float) -> float:

    std_dev = margin_of_error / 2
    return random.gauss(polling_value, std_dev)