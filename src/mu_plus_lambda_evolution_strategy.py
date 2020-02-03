import numpy as np
from src.utils import standard_value_mutation
from src.evolutionary_algorithm_abstract import *


class EvolutionStrategy(EvolutionaryAlgorithm):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate, step_method, selection_method):
        super().__init__(array_size, number_of_colors, population_size, offspring_size, mutation_rate, step_method, selection_method)
        self.offspring = None

    def mutate_random_parent(self):
        parent_id = np.random.randint(self.population_size)

        return np.fromiter((standard_value_mutation(x, self.step_method.step_function, self.mutation_rate)
                           for x in self.population[parent_id]), np.int)

    def variation(self):
        self.offspring = [self.mutate_random_parent() for _ in range(self.offspring_size)]

    def generate_filename_string(self):
        return "mu_plus_lambda_evolution_strategy_mu={}_lambda={}_array_size={}_number_of_colors={}".format(self.population_size,
                                                                                                            self.offspring_size,
                                                                                                            self.array_size,
                                                                                                            self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {} {} {}".format(self.array_size, self.number_of_colors, self.population_size, self.offspring_size, self.black_box.number_of_call_made)
