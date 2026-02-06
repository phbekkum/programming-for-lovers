import random

def simulate_one_election(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    margin_of_error: float
) -> tuple[int, int]:

    votes_candidate1 = 0
    votes_candidate2 = 0

    for state, poll_value in polls.items():

        if margin_of_error == 0.0:
            noisy_percentage = poll_value
        else:
            noisy_percentage = add_noise(poll_value, margin_of_error)

        if noisy_percentage >= 0.5:
            votes_candidate1 += electoral_votes[state]
        else:
            votes_candidate2 += electoral_votes[state]

    return votes_candidate1, votes_candidate2