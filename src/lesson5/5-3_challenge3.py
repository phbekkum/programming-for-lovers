import random

def add_noise(polling_value: float, margin_of_error: float) -> float:
    return random.gauss(polling_value, margin_of_error / 2)


def simulate_one_election(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    margin_of_error: float
) -> tuple[int, int]:

    votes0 = 0  # candidate 0
    votes1 = 0  # candidate 1

    for state, poll_value in polls.items():

        if margin_of_error == 0.0:
            noisy_value = poll_value
        else:
            noisy_value = add_noise(poll_value, margin_of_error)

        if noisy_value > 0.5:
            votes0 += electoral_votes[state]
        else:
            votes1 += electoral_votes[state]

    return votes0, votes1


def simulate_multiple_elections(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    num_trials: int,
    margin_of_error: float
) -> tuple[float, float, float]:

    wins0 = 0
    wins1 = 0
    ties = 0

    for _ in range(num_trials):
        votes0, votes1 = simulate_one_election(polls, electoral_votes, margin_of_error)

        if votes0 > votes1:
            wins0 += 1
        elif votes1 > votes0:
            wins1 += 1
        else:
            ties += 1

    probability0 = wins0 / num_trials
    probability1 = wins1 / num_trials
    probabilityTie = ties / num_trials

    return probability0, probability1, probabilityTie