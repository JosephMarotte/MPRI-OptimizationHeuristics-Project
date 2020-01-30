from utils import generate_random_disposition


class EvolutionaryAlgorithm:
    array_to_guess = None
    array_size = None
    number_of_call_made = None
    number_of_colors = None
    population_size = None
    offspring_size = None
    population = None
    population_fitness = None
    offspring = None
    offspring_fitness = None

    def __init__(self, array_size, number_of_colors, population_size, offspring_size):
        self.array_size = array_size
        self.number_of_colors = number_of_colors
        self.population_size = population_size
        self.offspring_size = offspring_size

    def set_array_to_guess(self, array_to_guess):
        self.number_of_call_made = 0
        self.array_to_guess = array_to_guess

    def generate_initial_population(self):
        population = [generate_random_disposition(self.array_size, self.number_of_colors) for _ in range(self.population_size)]

    def variation(self):
        raise NotImplementedError

    def evaluate_fitness_population(self):
        raise NotImplementedError

    def evaluate_fitness_offspring(self):
        raise NotImplementedError

    def selection(self):
        raise NotImplementedError

    def loop_condition(self):
        raise NotImplementedError

    def evolutionary_algorithm(self):
        self.generate_initial_population()
        self.evaluate_fitness_population()

        while self.loop_condition():
            self.offspring = self.variation()
            self.evaluate_fitness_offspring()
            self.selection()
