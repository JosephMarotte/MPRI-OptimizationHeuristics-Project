import pathlib
from src.one_plus_mu_plus_lambda_genetic_algorithm import GeneticAlgorithm, GeneticAlgorithmAdaptive
from src.step_functions import StepFactory, UNIFORM_MUTATION
from src.selection_functions import SelectionFactory, ELITIST_SELECTION


def retrieve_value_one_plus_mu_lambda_ga(lambd, number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "GA_1_plus_mu_lambda.csv"

    for nb_of_color in number_of_colors:
        step_method = StepFactory(nb_of_color, UNIFORM_MUTATION)
        selection_method = SelectionFactory(ELITIST_SELECTION)
        alg = GeneticAlgorithm(nb_of_color, nb_of_color, lambd, min(1, lambd / nb_of_color), 1 / lambd, step_method, selection_method)
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break


def retrieve_value_one_plus_mu_lambda_adaptive_ga(initial_lambda, update_strength, number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "GA_1_plus_mu_lambda_adaptive.csv"
    for nb_of_color in number_of_colors:
        step_method = StepFactory(nb_of_color, UNIFORM_MUTATION)
        selection_method = SelectionFactory(ELITIST_SELECTION)
        alg = GeneticAlgorithmAdaptive(nb_of_color, nb_of_color, min(nb_of_color, initial_lambda), update_strength, step_method, selection_method)
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break
