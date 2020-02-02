import numpy as np
from src.utils import *
from src.mastermind_problem import MasterMindProblemAbstract


# Random local search on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
class RandomLocalSearch(MasterMindProblemAbstract):
    def __init__(self, array_size, number_of_colors, step_method):
        super().__init__(array_size, number_of_colors)
        self.step_method = step_method

    def random_local_search(self):
        self.number_of_call_made += 1
        guess = generate_random_disposition(self.array_size, self.number_of_colors)
        current_number_of_equals_elements = self.black_box.evaluate(guess)
        while current_number_of_equals_elements != self.array_size:
            id_to_modify = np.random.randint(self.array_size)

            old_color = guess[id_to_modify]
            guess[id_to_modify] = self.step_method(old_color)

            new_current_number_of_equals_elements = self.black_box.evaluate(guess)
            if new_current_number_of_equals_elements > current_number_of_equals_elements:
                current_number_of_equals_elements = new_current_number_of_equals_elements
            else:
                guess[id_to_modify] = old_color

    def algorithm(self):
        self.random_local_search()

    def generate_filename_string(self):
        return "randomLocalSearch_array_size={}_number_of_colors={}".format(self.array_size, self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {}".format(self.array_size, self.number_of_colors, self.number_of_call_made)
