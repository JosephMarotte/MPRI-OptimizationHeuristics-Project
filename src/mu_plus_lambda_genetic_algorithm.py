import numpy as np
import operator
from utils import standard_value_mutation
from evolutionary_algorithm_abstract import *


class GeneticAlgorithm(EvolutionaryAlgorithm):
    mutation_rate = None

    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate, k_parents):
        assert (mutation_rate < 1)
        assert (mutation_rate > 0)
        super().__init__(array_size, number_of_colors, population_size, offspring_size)
        self.mutation_rate = mutation_rate
        self.k_parents = k_parents

    def crossover_single_offspring(self):
        # select k distinct parents for the crossover
        parents_id = np.random.choice(self.population_size, self.k_parents, replace=False)
        # for each color chose randomly one of the parents
        return np.fromiter((self.population[parents_id[np.random.randint(self.k_parents)]][i] for i in range(self.array_size)), np.int)

    def crossover(self):
        self.offspring = [self.crossover_single_offspring() for _ in range(self.offspring_size)]

    def mutate_single_offspring(self, offspring):
        return np.fromiter((standard_value_mutation(x, self.number_of_colors, self.mutation_rate) for x in offspring), np.int)

    def mutate(self):
        self.offspring = [self.mutate_single_offspring(offspring) for offspring in self.offspring]

    def variation(self):
        self.crossover()
        self.mutate()

    def selection(self):
        raise NotImplementedError


class GeneticAlgorithmSelectingOffspring(GeneticAlgorithm):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        self.comma_selection()


class GeneticAlgorithmSelectingPopulationAndOffspring(GeneticAlgorithm):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        self.elitist_selection()