import numpy as np
from src.utils import standard_value_mutation
from src.evolutionary_algorithm_abstract import *
from math import ceil


class GeneticAlgorithm(EvolutionaryAlgorithm):
    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate, crossover_probability, update_strength, step_method):
        super().__init__(array_size, number_of_colors, population_size, offspring_size, mutation_rate, step_method)
        self.crossover_probability = crossover_probability
        self.update_strength = update_strength

    def mutate_disposition(self, disposition):
        return np.fromiter((standard_value_mutation(x, self.step_method.step_function, self.mutation_rate)
                            for x in disposition), np.int)

    def mutate(self):
        self.offspring = [self.mutate_disposition(self.population[0]) for _ in self.offspring_size]

    def crossover_disposition(self, disposition1, disposition2):
        assert(len(disposition1) == len(disposition2))
        return [x if np.random.random() <= self.crossover_probability else y for x, y in zip(disposition1, disposition2)]

    def crossover(self):
        self.offspring = [self.crossover_disposition(self.population[0], offspring) for offspring in self.offspring]

    def variation(self):
        self.crossover()
        self.mutate()

    def variation(self):
        self.mutate()
        self.crossover()

    def selection(self):
        old_population_fitness = self.population_fitness[0]
        self.elitist_selection()
        if self.population_fitness[0] > old_population_fitness:
            self.offspring_size = max(self.offspring_size / self.update_strength, 1)
        else:
            self.offspring_size = min(ceil(self.offspring_size * pow(self.update_strength, 0.25)), self.array_size)

    def generate_filename_string(self):
        return "one_plu_mu_comma_lambda_genetic_algorithm_mu={}_lambda={}_array_size={}_number_of_colors={}".format(self.population_size,
                                                                                                                    self.offspring_size,
                                                                                                                    self.array_size,
                                                                                                                    self.number_of_colors)

    def generate_configuration_result(self):
        return "{} {} {} {} {}".format(self.array_size, self.number_of_colors, self.population_size, self.offspring_size, self.black_box.number_of_call_made)
