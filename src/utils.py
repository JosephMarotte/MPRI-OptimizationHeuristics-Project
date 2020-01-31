import numpy as np


# Generate random array to guess
def generate_random_disposition(size_of_the_array, number_of_colors):
    return np.random.random_integers(0, number_of_colors - 1, size_of_the_array)


# Count the number of equals elements in the two arrays
def number_of_equals_elements(guess, array_to_guess):
    assert (len(guess) == len(array_to_guess))
    return np.count_nonzero(guess == array_to_guess)


# Mutate a color given a mutation rate and the number of colors
def standard_value_mutation(previous_color, number_of_colors, mutation_rate):
    if np.random.random() <= mutation_rate:
        new_color = np.random.randint(0, number_of_colors)
        while new_color == previous_color:
            new_color = np.random.randint(0, number_of_colors)
        return new_color
    return previous_color
