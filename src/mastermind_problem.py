import pathlib
from src.blackbox import BlackBox


class MasterMindProblemAbstract:
    array_size = None
    number_of_colors = None

    black_box = None

    def __init__(self, array_size, number_of_colors):
        self.array_size = array_size
        self.number_of_colors = number_of_colors
        self.black_box = BlackBox(array_size, number_of_colors)

    def solve(self, array_to_guess=None):
        self.black_box.new_session(array_to_guess)
        self.algorithm()

    def algorithm(self):
        raise NotImplementedError

    def generate_filename_string(self):
        raise NotImplementedError

    def generate_configuration_result(self):
        raise NotImplementedError

    def test_performance(self, number_of_iterations, filename=None, open_mode=None):
        if filename is None:
            path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/"
            pathlib.Path(path_to_result_dir).mkdir(parents=True, exist_ok=True)
            filename = path_to_result_dir + self.generate_filename_string()
        if open_mode is None:
            open_mode = 'w'
        with open(filename, open_mode) as file:
            for i in range(number_of_iterations):
                self.solve()
                self.store_result(file)

    def store_result(self, file):
        file.write(self.generate_configuration_result() + '\n')
