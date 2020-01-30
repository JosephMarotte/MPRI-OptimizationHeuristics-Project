import numpy as np
import operator
from evolutionary_algorithm_abstract import *
from utils import number_of_equals_elements


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

    def evaluate_fitness(self, array_to_evaluate):
        self.number_of_call_made += len(array_to_evaluate)
        return np.fromiter((number_of_equals_elements(x, self.array_to_guess) for x in array_to_evaluate), np.int)

    def evaluate_fitness_population(self):
        self.population_fitness = self.evaluate_fitness(self.population)

    def evaluate_fitness_offspring(self):
        self.offspring_fitness = self.evaluate_fitness(self.offspring)

    def loop_condition(self):
        return self.population[-1] == self.array_size  # compare max of population with goal

    def selection(self):
        raise NotImplementedError


class EvolutionStrategySelectingOffspring(EvolutionStrategy):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        zipped = list(zip(self.offspring_fitness, self.offspring))
        zipped = sorted(zipped, key=operator.itemgetter(1))
        zipped = zipped[:-self.population_size]
        self.population_fitness, self.population = zip(*zipped)  # unzip


class EvolutionStrategySelectingPopulationAndOffspring(EvolutionStrategy):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate):
        assert(offspring_size >= population_size)
        super().__init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate)

    def selection(self):
        # TODO could be improved because we know self.population is already sorted
        fitness = np.concatenate(self.offspring_fitness, self.population_fitness)
        population = np.concatenate(self.offspring, self.population)
        zipped = list(zip(fitness, population))
        zipped = sorted(zipped, key=operator.itemgetter(1))
        zipped = zipped[:-self.population_size]
        self.population_fitness, self.population = zip(*zipped)  # unzip


def compute_new_guess(guess, number_of_colors, mutation_rate):
    return np.fromiter((standard_value_mutation(x, number_of_colors, mutation_rate) for x in guess), np.int)


def standard_value_mutation(previous_color, number_of_colors, mutation_rate):
    if np.random.random() <= mutation_rate:
        new_color = np.random.randint(0, number_of_colors)
        while new_color == previous_color:
            new_color = np.random.randint(0, number_of_colors)
        return new_color
    return previous_color
