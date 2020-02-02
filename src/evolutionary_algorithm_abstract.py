import operator
import numpy as np
from src.utils import *
from src.mastermind_problem import MasterMindProblemAbstract


class EvolutionaryAlgorithm(MasterMindProblemAbstract):
    array_to_guess = None
    array_size = None
    number_of_colors = None
    population_size = None
    offspring_size = None
    population = None
    population_fitness = None
    offspring = None
    offspring_fitness = None
    step_method = None
    mutation_rate = None

    def __init__(self, array_size, number_of_colors, population_size, offspring_size, mutation_rate, step_method):
        super().__init__(array_size, number_of_colors)
        assert (mutation_rate < 1)
        assert (mutation_rate > 0)
        self.population_size = population_size
        self.offspring_size = offspring_size
        self.step_method = step_method
        self.mutation_rate = mutation_rate

    def generate_initial_population(self):
        self.population = [generate_random_disposition(self.array_size, self.number_of_colors) for _ in range(self.population_size)]

    def variation(self):
        raise NotImplementedError

    def evaluate_fitness(self, dispositions_to_evaluate):
        return np.fromiter((self.black_box.evaluate(disposition) for disposition in dispositions_to_evaluate), np.int)

    def evaluate_fitness_population(self):
        self.population_fitness = self.evaluate_fitness(self.population)

    def evaluate_fitness_offspring(self):
        self.offspring_fitness = self.evaluate_fitness(self.offspring)

    def comma_selection(self):
        zipped = list(zip(self.offspring_fitness, self.offspring))
        zipped = sorted(zipped, key=operator.itemgetter(1))
        zipped = zipped[-self.population_size:]
        self.population_fitness, self.population = zip(*zipped)  # unzip

    def elitist_selection(self):
        self.offspring_fitness = np.array(self.offspring_fitness)
        self.population_fitness = np.array(self.population_fitness)
        fitness = np.concatenate((self.offspring_fitness, self.population_fitness))
        population = np.concatenate((self.offspring, self.population))
        zipped = list(zip(fitness, population))
        zipped = sorted(zipped, key=operator.itemgetter(0))
        zipped = zipped[-self.population_size:]
        self.population_fitness, self.population = zip(*zipped)  # unzip

    def selection(self):
        raise NotImplementedError

    def loop_condition(self):
        return self.population_fitness[-1] < self.array_size  # compare max of population with goal

    def generate_filename_string(self):
        raise NotImplementedError

    def generate_configuration_result(self):
        raise NotImplementedError

    def algorithm(self):
        self.generate_initial_population()
        self.evaluate_fitness_population()

        while self.loop_condition():
            self.variation()
            self.evaluate_fitness_offspring()
            self.selection()
