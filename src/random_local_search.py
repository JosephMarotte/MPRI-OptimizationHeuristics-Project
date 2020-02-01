import numpy as np
from src.utils import *


# Random local search on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
def random_local_search(size_of_the_array, number_of_colors, array_to_guess):
    number_of_call_made = 1
    guess = generate_random_disposition(size_of_the_array, number_of_colors)
    current_number_of_equals_elements = number_of_equals_elements(guess, array_to_guess)
    while current_number_of_equals_elements != size_of_the_array:
        number_of_call_made += 1
        id_to_modify = np.random.randint(0, size_of_the_array)
        old_color = guess[id_to_modify]
        new_color = np.random.randint(0, number_of_colors)
        while new_color == old_color:
            new_color = np.random.randint(0, number_of_colors)
        guess[id_to_modify] = new_color

        new_current_number_of_equals_elements = number_of_equals_elements(guess, array_to_guess)
        if new_current_number_of_equals_elements > current_number_of_equals_elements:
            current_number_of_equals_elements = new_current_number_of_equals_elements
        else:
            guess[id_to_modify] = old_color
    return number_of_call_made
