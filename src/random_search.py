from utils import *
from mastermind_problem import MasterMindProblemAbstract


# Random search on the disposition to guess
# Returns the number of calls to number_of_equals_elements made
class RandomSearch(MasterMindProblemAbstract):
    def __init__(self, array_size, number_of_colors):
        super().__init__(array_size, number_of_colors)

    def random_search(self):
        guess = generate_random_disposition(self.array_size, self.number_of_colors)
        while self.black_box.evaluate(guess) != self.black_box.max_possible_evaluation:
            guess = generate_random_disposition(self.array_size, self.number_of_colors)

    def algorithm(self):
        self.random_search()

    def generate_filename_string(self):
        return "randomSearch_array_size={}_number_of_colors={}".format(self.array_size, self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {}".format(self.array_size, self.number_of_colors, self.black_box.number_of_call_made)
