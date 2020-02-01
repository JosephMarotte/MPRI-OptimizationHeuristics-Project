from utils import generate_random_disposition, number_of_equals_elements, get_smallest_greater_disposition
from math import exp, ceil, log
import numpy as np


class ErdosRenyiHasMultipleSolution(Exception):
    pass


# ErdosRenyi adapted solution to n colors
# Pick a number of random disposition and check their number of equals elements with the disposition to guess
# For every possible disposition for every random disposition previously picked, check whether the number of equals
#   elements is the same as for the disposition to guess
class ErdosRenyiLike:
    array_size = None
    number_of_colors = None
    number_of_call_made = None
    array_to_guess = None

    def __init__(self, array_size, number_of_colors):
        self.array_size = array_size
        self.number_of_colors = number_of_colors

    def set_array_to_guess(self, array_to_guess):
        self.number_of_call_made = 0
        self.array_to_guess = array_to_guess

    def algorithm(self):
        assert (self.array_to_guess is not None)
        max_number_of_call_needed = ceil(2 * exp(1) * self.array_size * (log(self.array_size, 2) + 1))
        picked_disposition = [generate_random_disposition(self.size_of_the_array, self.number_of_colors)
                              for _ in range(max_number_of_call_needed)]
        picked_disposition_fitness = [number_of_equals_elements(guess, self.array_to_guess)
                                      for guess in picked_disposition]

        possible_answers = []
        max_number_of_disposition_needed = 0

        current_disposition_checked = np.zeros(self.array_size)
        for i in range(pow(self.number_of_colors, self.array_size) - 1):
            is_possible_solution = True
            for id_disposition, (disposition, fitness) in enumerate(zip(picked_disposition, picked_disposition_fitness)):
                if number_of_equals_elements(current_disposition_checked, disposition) != picked_disposition_fitness:
                    is_possible_solution = False
                    max_number_of_disposition_needed = max(max_number_of_disposition_needed, id_disposition + 1)
                    break
            if is_possible_solution:
                possible_answers.append(np.copy(current_disposition_checked))
            current_disposition_checked = get_smallest_greater_disposition(current_disposition_checked,
                                                                           self.number_of_colors)

        if len(possible_answers) != 1:
            raise ErdosRenyiHasMultipleSolution

        self.number_of_call_made = max_number_of_disposition_needed
        return max_number_of_disposition_needed

    def compute_number_of_call_needed(self, array_to_guess):
        self.set_array_to_guess(array_to_guess)
        self.algorithm()
        return self.number_of_call_made
