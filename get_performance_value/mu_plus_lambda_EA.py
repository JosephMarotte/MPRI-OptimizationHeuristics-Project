import pathlib
from src.mu_plus_lambda_evolution_strategy import EvolutionStrategy
from src.step_functions import StepFactory, UNIFORM_MUTATION
from src.selection_functions import SelectionFactory, ELITIST_SELECTION

path_to_result_dir = str(pathlib.Path(__file__).parent.parent.absolute()) + "/results/" + "EA_mu_lambda"


def retrieve_value_one_plus_one_ea():
    val_i = [pow(2, i) for i in range(1, 8)]
    for i in val_i:
        step_method = StepFactory(i, UNIFORM_MUTATION)
        selection_method = SelectionFactory(ELITIST_SELECTION)
        alg = EvolutionStrategy(i, i, 1, 1, 1/i, step_method, selection_method)
        alg.test_performance(15, filename=path_to_result_dir, open_mode='a')


retrieve_value_one_plus_one_ea()
