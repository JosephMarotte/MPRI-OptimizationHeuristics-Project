import numpy as np
import operator

ELITIST_SELECTION = "ELITIST_SELECTION"
COMMA_SELECTION = "COMMA_SELECTION"


class SelectionFactory:
    def __init__(self, selection_name):
        self.selection_function = selection_name
        if selection_name == COMMA_SELECTION:
            self.selection_function = self.comma_selection
        elif selection_name == ELITIST_SELECTION:
            self.selection_function = self.elitist_selection
        else:
            raise Exception

    @staticmethod
    def comma_selection(evolution_algorithm):
        zipped = list(zip(evolution_algorithm.offspring_fitness, evolution_algorithm.offspring))
        zipped = sorted(zipped, key=operator.itemgetter(1))
        zipped = zipped[-evolution_algorithm.population_size:]
        return zip(*zipped)  # unzip

    @staticmethod
    def elitist_selection(evolution_algorithm):
        fitness = np.concatenate((evolution_algorithm.offspring_fitness, evolution_algorithm.population_fitness))
        population = np.concatenate((evolution_algorithm.offspring, evolution_algorithm.population))
        zipped = list(zip(fitness, population))
        zipped = sorted(zipped, key=operator.itemgetter(0))
        # we need to shuffle the array to not always take the element from population in case the fitness was improved
        fitness_threshold = zipped[-evolution_algorithm.population_size][0]
        zipped = list(filter(lambda t: t[0] >= fitness_threshold, zipped))
        np.random.shuffle(zipped)
        zipped = zipped[-evolution_algorithm.population_size:]
        return zip(*zipped)  # unzip
