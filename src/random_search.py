from utils import *


# Random search on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
def random_search(size_of_the_array, number_of_colors, array_to_guess):
    number_of_call_made = 1
    guess = generate_random_disposition(size_of_the_array, number_of_colors)
    while number_of_equals_elements(guess, array_to_guess) != size_of_the_array:
        guess = generate_random_disposition(size_of_the_array, number_of_colors)
        number_of_call_made += 1
    return number_of_call_made
