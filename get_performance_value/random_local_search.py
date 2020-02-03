import pathlib
from src.random_local_search import RandomLocalSearch
from src.step_functions import StepFactory, UNIFORM_MUTATION

path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "RLS_UNIFORM_MUTATION"


def retrieve_value_random_local_search():
    val_i = [pow(2, i) for i in range(1, 8)]
    for i in val_i:
        alg = RandomLocalSearch(i, i, StepFactory(i, UNIFORM_MUTATION))
        alg.test_performance(15, filename=path_to_result_dir, open_mode='a')


# retrieve_value_random_local_search()