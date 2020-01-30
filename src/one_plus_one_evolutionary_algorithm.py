import numpy as np
from utils import *


# (1+1)EA on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
def one_plus_one_evolutionary_algorithm(size_of_the_array, number_of_colors, array_to_guess, mutation_rate):
    assert (mutation_rate < 1)
    assert (mutation_rate > 0)
    number_of_call_made = 1
    guess = generate_random_disposition(size_of_the_array, number_of_colors)
    current_number_of_equals_elements = number_of_equals_elements(guess, array_to_guess)
    while current_number_of_equals_elements != size_of_the_array:
        number_of_call_made += 1
        new_guess = compute_new_guess(guess, number_of_colors, mutation_rate)
        new_current_number_of_equals_elements = number_of_equals_elements(new_guess, array_to_guess)
        if new_current_number_of_equals_elements > current_number_of_equals_elements:
            current_number_of_equals_elements = new_current_number_of_equals_elements
            guess = new_guess
    return number_of_call_made


def compute_new_guess(guess, number_of_colors, mutation_rate):
    return np.fromiter((standard_value_mutation(x, number_of_colors, mutation_rate) for x in guess), np.int)


def standard_value_mutation(previous_color, number_of_colors, mutation_rate):
    if np.random.random() <= mutation_rate:
        new_color = np.random.randint(0, number_of_colors)
        while new_color == previous_color:
            new_color = np.random.randint(0, number_of_colors)
        return new_color
    return previous_color
