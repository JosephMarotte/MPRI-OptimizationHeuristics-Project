from src.utils import generate_random_disposition, number_of_equals_elements, get_smallest_greater_disposition
from src.mastermind_problem import MasterMindProblemAbstract
from math import exp, ceil, log
import numpy as np


class ErdosRenyiHasMultipleSolution(Exception):
    pass


# ErdosRenyi adapted solution to n colors
# Pick a number of random disposition and check their number of equals elements with the disposition to guess
# For every possible disposition for every random disposition previously picked, check whether the number of equals
#   elements is the same as for the disposition to guess
class ErdosRenyiLike(MasterMindProblemAbstract):
    def __init__(self, array_size, number_of_colors):
        super().__init__(array_size, number_of_colors)

    def algorithm(self):
        assert (self.black_box.disposition is not None)
        max_number_of_call_needed = ceil(2 * exp(1) * self.array_size * (log(self.array_size, 2) + 1))
        picked_disposition = [generate_random_disposition(self.array_size, self.number_of_colors)
                              for _ in range(max_number_of_call_needed)]
        picked_disposition_fitness = [number_of_equals_elements(guess, self.black_box.disposition)
                                      for guess in picked_disposition]

        possible_answers = []
        max_number_of_disposition_needed = 0

        current_disposition_checked = np.zeros(self.array_size)
        for i in range(pow(self.number_of_colors, self.array_size)):
            is_possible_solution = True
            for id_disposition, (disposition, fitness) in enumerate(zip(picked_disposition, picked_disposition_fitness)):
                if number_of_equals_elements(current_disposition_checked, disposition) != picked_disposition_fitness[id_disposition]:
                    is_possible_solution = False
                    max_number_of_disposition_needed = max(max_number_of_disposition_needed, id_disposition + 1)
                    break
            if is_possible_solution:
                possible_answers.append(np.copy(current_disposition_checked))
            current_disposition_checked = get_smallest_greater_disposition(current_disposition_checked,
                                                                           self.number_of_colors)

        if len(possible_answers) != 1:
            raise ErdosRenyiHasMultipleSolution

        self.black_box.number_of_call_made = max_number_of_disposition_needed
        return max_number_of_disposition_needed

    def generate_filename_string(self):
        return "erdosRenyiLike_array_size={}_number_of_colors={}".format(self.array_size, self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {}".format(self.array_size, self.number_of_colors, self.black_box.number_of_call_made)
