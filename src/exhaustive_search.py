import numpy as np
from src.utils import number_of_equals_elements, get_smallest_greater_disposition, generate_random_disposition
from src.src.src.src.src.src.src.src.src.mastermind_problem import MasterMindProblemAbstract


# Exhaustive search on the array_to_guess
# Returns the number of calls to number_of_equals_elements made
class ExhaustiveSearch(MasterMindProblemAbstract):
    def __init__(self, array_size, number_of_colors):
        super().__init__(array_size, number_of_colors)

    def exhaustive_search(self):
        guess = np.zeros(self.array_size)
        while self.black_box.evaluate(guess) != self.black_box.max_possible_evaluation:
            guess = get_smallest_greater_disposition(guess, self.number_of_colors)

    def algorithm(self):
        self.exhaustive_search()

    def generate_filename_string(self):
        return "exhaustiveSearch_array_size={}_number_of_colors={}".format(self.array_size, self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {}".format(self.array_size, self.number_of_colors, self.black_box.number_of_call_made)
