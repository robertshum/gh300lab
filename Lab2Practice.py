import random


def sum_squares_of_first_10_integers():
    """Return the sum of the squares of the integers from 1 through 10."""
    # The upper bound is exclusive, so use 11 to include the integer 10.
    return sum(number ** 2 for number in range(1, 11))


def random_compliment(name):
    """Return a randomly selected compliment addressed to name."""
    compliments = [
        f"{name}, you have a wonderful sense of humor.",
        f"{name}, your creativity is inspiring.",
        f"{name}, you make people feel welcome.",
        f"{name}, you bring great energy to everything you do.",
        f"{name}, you are thoughtful and kind.",
    ]
    # Select one of the five personalized compliments at random.
    return random.choice(compliments)
