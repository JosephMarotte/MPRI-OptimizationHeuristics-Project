import pathlib
from src.utils import generate_random_disposition


class MasterMindProblemAbstract:
    array_size = None
    number_of_colors = None

    array_to_guess = None
    number_of_call_made = None

    def __init__(self, array_size, number_of_colors):
        self.array_size = array_size
        self.number_of_colors = number_of_colors

    def set_array_to_guess(self, array_to_guess):
        assert(max(array_to_guess) < self.number_of_colors)
        self.array_size = len(array_to_guess)
        self.number_of_call_made = 0
        self.array_to_guess = array_to_guess

    def solve(self, array_to_guess=None):
        if array_to_guess is None:
            array_to_guess = generate_random_disposition(self.array_size, self.number_of_colors)
        self.set_array_to_guess(array_to_guess)
        self.algorithm()

    def algorithm(self):
        raise NotImplementedError

    def generate_filename_string(self):
        raise NotImplementedError

    def generate_configuration_result(self):
        raise NotImplementedError

    def test_performance(self, number_of_iterations, filename=None):
        if filename is None:
            path_to_result_dir = str(pathlib.Path(__file__).parent.absolute()) + "/results/"
            pathlib.Path(path_to_result_dir).mkdir(parents=True, exist_ok=True)
            filename = path_to_result_dir + self.generate_filename_string()
        with open(filename, 'w') as file:
            for i in range(number_of_iterations):
                self.solve()
                self.store_result(file)

    def store_result(self, file):
        file.write(self.generate_configuration_result() + '\n')
