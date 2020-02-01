import numpy as np
from utils import number_of_equals_elements, get_smallest_greater_disposition


# Exhaustive search on the array_to_guess
# Returns the number of calls to number_of_equals_elements made
def exhaustive_search(size_of_the_array, number_of_colors, array_to_guess):
    guess = np.zeros(size_of_the_array)
    number_of_call_made = 1
    while number_of_equals_elements(size_of_the_array, array_to_guess) != size_of_the_array:
        number_of_call_made += 1
        guess = get_smallest_greater_disposition(guess, number_of_colors)
    return number_of_call_made
