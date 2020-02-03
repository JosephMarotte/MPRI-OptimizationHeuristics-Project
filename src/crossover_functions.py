import numpy as np

UNIFORM_CROSSOVER = "uniform_crossover"
NON_UNIFORM_CROSSOVER = "non_uniform_crossover"
MAJORITY_VOTE_CROSSOVER = "majority_vote_crossover"


class Crossover:
    crossover_name = None
    crossover_function = None

    def __init__(self, crossover_name, crossover_function):
        self.crossover_name = crossover_name
        self.crossover_function = crossover_function


class CrossoverFactory:
    @staticmethod
    def get_crossover(crossover_name, crossover_probability=0.5):
        if crossover_name == UNIFORM_CROSSOVER:
            return Crossover(crossover_name, lambda x: CrossoverFactory.non_uniform_crossover(x, 0.5))
        elif crossover_name == NON_UNIFORM_CROSSOVER:
            return Crossover(crossover_name, lambda x: CrossoverFactory.non_uniform_crossover(x, crossover_probability))
        elif crossover_name == MAJORITY_VOTE_CROSSOVER:
            return Crossover(crossover_name, CrossoverFactory.majority_vote)
        else:
            raise Exception

    @staticmethod
    def non_uniform_crossover(crossover_points, crossover_probability):
        return [x if np.random.random() <= crossover_probability else y
                for x, y in zip(crossover_points[0], crossover_points[1])]

    @staticmethod
    def uniform_crossover(crossover_points):
        return [x if np.random.random() <= 0.5 else y for x, y in zip(crossover_points[0], crossover_points[1])]

    @staticmethod
    def majority_vote(crossover_points):
        return [crossover_points[np.random.randint(0, len(crossover_points))][i] for i in range(crossover_points[0])]


