from src.utils import *
from src.mastermind_problem import MasterMindProblemAbstract


# Random search on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
class RandomSearch(MasterMindProblemAbstract):
    def __init__(self, array_size, number_of_colors):
        super().__init__(array_size, number_of_colors)

    def random_search(self):
        self.number_of_call_made += 1
        guess = generate_random_disposition(self.array_size, self.number_of_colors)
        while number_of_equals_elements(guess, self.array_to_guess) != self.array_size:
            guess = generate_random_disposition(self.array_size, self.number_of_colors)
            self.number_of_call_made += 1

    def algorithm(self):
        self.random_search()

    def generate_filename_string(self):
        return "randomSearch_array_size={}_number_of_colors={}".format(self.array_size, self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {}".format(self.array_size, self.number_of_colors, self.number_of_call_made)
