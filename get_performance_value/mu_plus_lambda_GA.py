import pathlib
from src.mu_plus_lambda_genetic_algorithm import GeneticAlgorithm
from src.step_functions import StepFactory, UNIFORM_MUTATION
from src.selection_functions import SelectionFactory, ELITIST_SELECTION


def retrieve_value_mu_plus_lambda_ga(mu, lambd, k_center, number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "GA_mu_lambda"

    for nb_of_color in number_of_colors:
        step_method = StepFactory(nb_of_color, UNIFORM_MUTATION)
        selection_method = SelectionFactory(ELITIST_SELECTION)
        alg = GeneticAlgorithm(nb_of_color, nb_of_color, mu, lambd, 1/nb_of_color, step_method, selection_method, k_center)
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break
