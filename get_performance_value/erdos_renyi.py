import pathlib
from src.erdos_renyi_like import ErdosRenyiLike


def retrieve_value_erdos_renyi(number_of_colors):
    path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "erdos_renyi"

    for nb_of_color in number_of_colors:
        alg = ErdosRenyiLike(nb_of_color, nb_of_color)
        if alg.test_performance(15, filename=path_to_result_dir, open_mode='a'):
            break
