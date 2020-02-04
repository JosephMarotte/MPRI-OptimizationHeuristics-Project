import pathlib
from src.random_local_search import RandomLocalSearch
from src.step_functions import StepFactory, UNIFORM_MUTATION


def retrieve_value_random_local_search(number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "RLS_UNIFORM_MUTATION.csv"

    for nb_of_color in number_of_colors:
        alg = RandomLocalSearch(nb_of_color, nb_of_color, StepFactory(nb_of_color, UNIFORM_MUTATION))
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break
