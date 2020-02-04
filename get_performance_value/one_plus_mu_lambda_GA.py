import pathlib
from src.one_plus_mu_plus_lambda_genetic_algorithm import GeneticAlgorithmAdaptive
from src.step_functions import StepFactory, UNIFORM_MUTATION
from src.selection_functions import SelectionFactory, ELITIST_SELECTION

path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "GA_1_plus_mu_lambda"


def retrieve_value_mu_plus_lambda_ga():
    val_i = [pow(2, i) for i in range(1, 8)]
    for i in val_i:
        step_method = StepFactory(i, UNIFORM_MUTATION)
        selection_method = SelectionFactory(ELITIST_SELECTION)
        alg = GeneticAlgorithmAdaptive(i, i, min(i, 10), min(i, 10), 1.4, step_method, selection_method)
        alg.test_performance(15, filename=path_to_result_dir, open_mode='a')


retrieve_value_mu_plus_lambda_ga()
