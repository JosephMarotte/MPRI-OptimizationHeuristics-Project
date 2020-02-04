import pathlib
from src.exhaustive_search import ExhaustiveSearch


def retrieve_value_exhaustive_search(number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "exhaustive_search"

    for nb_of_color in number_of_colors:
        alg = ExhaustiveSearch(nb_of_color, nb_of_color)
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break
