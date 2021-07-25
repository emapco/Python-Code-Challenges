from random import randint, randrange
from collections import Counter

# function to determine the probability of certain outcomes when rolling dice
# via a Monte Carlo simulation
def roll_dice(*die, simulation_count=1_000_000):
    # initialize dictionary
    min_roll = len(die)
    max_roll = sum(die)+1
    occurrences = {i: 0 for i in range(min_roll, max_roll + 1)}

    # roll each dice and sum them, simulation_count amount of times
    # and increment summed occurrence by one
    for i in range(simulation_count):
        occurrences[sum(randrange(1, dice+1) for dice in die)] += 1

    # calculate probabilities and print
    probabilities = {key: value / simulation_count * 100 for key, value in occurrences.items()}
    print("Outcome Probability")
    for key, value in probabilities.items():
        print("{:<3} {:.2f}%".format(key, value))


def solution(*dice, num_trials=1_000_000):
    counts = Counter()  # object to count the number of occurrences; basically a dictionary
    for roll in range(num_trials):
        # roll each dice and sums the rolls and increments the occurrences by one
        counts[sum((randint(1, sides) for sides in dice))] += 1

    print("\nOUTCOME\tPROBABILITY")
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))


if __name__ == '__main__':
    roll_dice(4, 6, 6)
    # solution(4, 6, 6)
