import numpy as np
from utils import number_of_equals_elements


# Exhaustive search on the array_to_guess
# Returns the number of calls to compare_array used
def exhaustive_search(size_of_the_array, number_of_color, array_to_guess):
    guess = np.zeros(size_of_the_array)
    number_of_call_made = 1
    while number_of_equals_elements(size_of_the_array, array_to_guess) != size_of_the_array:
        for i in range(size_of_the_array):
            number_of_call_made += 1
            guess[i] = (guess[i] + 1) % number_of_color
            if guess[i] == 0:
                break
    return number_of_call_made
