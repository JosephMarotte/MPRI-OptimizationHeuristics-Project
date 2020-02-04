import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.random_local_search import RandomLocalSearch
from src.step_functions import *
from src.mu_plus_lambda_evolution_strategy import *
from src.selection_functions import *
import numpy as np

"""
for n in range(5, 41, 2):
    r = EvolutionStrategy(n, n, 1, 1, 1 / n, 1.5, 0.9, StepFactory(n, UNIFORM_MUTATION), SelectionFactory("elitist_selection_1"))
    r.test_performance(20, open_mode="a+")
    print(n)
"""
probas = [2]
for p in probas:
    for n in range(3, 41, 2):
        r = EvolutionStrategy(n, n, 1, 1, p / n, 1, 1, StepFactory(n, UNIFORM_MUTATION), SelectionFactory(ELITIST_SELECTION))
        r.test_performance(10, open_mode="a+")
        print(n)
