import numpy as np


# Generate random array to guess
def generate_random_disposition(size_of_the_array, number_of_colors):
    return np.random.random_integers(0, number_of_colors - 1, size_of_the_array)


# Count the number of equals elements in the two arrays
def number_of_equals_elements(guess, array_to_guess):
    assert (len(guess) == len(array_to_guess))
    return np.count_nonzero(guess == array_to_guess)
