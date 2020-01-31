import numpy as np
from utils import standard_value_mutation
from evolutionary_algorithm_abstract import *


class EvolutionStrategy(EvolutionaryAlgorithm):
    mutation_rate = None

    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert (mutation_rate < 1)
        assert (mutation_rate > 0)
        super().__init__(array_size, number_of_colors, population_size, offspring_size)
        self.mutation_rate = mutation_rate

    def mutate_random_parent(self):
        parent_id = np.random.randint(self.population_size)
        return compute_new_guess(self.population[parent_id], self.number_of_colors, self.mutation_rate)

    def variation(self):
        self.offspring = [self.mutate_random_parent() for _ in range(self.offspring_size)]

    def selection(self):
        raise NotImplementedError


class EvolutionStrategySelectingOffspring(EvolutionStrategy):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        self.comma_selection()


class EvolutionStrategySelectingPopulationAndOffspring(EvolutionStrategy):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        self.elitist_selection()


def compute_new_guess(guess, number_of_colors, mutation_rate):
    return np.fromiter((standard_value_mutation(x, number_of_colors, mutation_rate) for x in guess), np.int)
