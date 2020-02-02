import numpy as np

UNIFORM_MUTATION = "uniform_mutation"
UNIT_MUTATION = "unit_mutation"
HARMONIC_MUTATION = "harmonic_mutation"


class StepFactory:
    @staticmethod
    def build_step(number_of_colors, step_name, array_mutation_strength):
        if step_name == UNIFORM_MUTATION:
            return lambda x: uniform_mutation_step(x, number_of_colors)
        elif step_name == UNIT_MUTATION:
            return lambda x: unit_mutation_step(x, number_of_colors)
        elif step_name == HARMONIC_MUTATION:
            return lambda x: harmonic_mutation_step(x, number_of_colors, array_mutation_strength)
        else:
            raise Exception


def uniform_mutation_step(previous_color, number_of_colors):
    new_color = (previous_color + np.random.randint(1, number_of_colors - 1)) % number_of_colors
    return new_color


def unit_mutation_step(previous_color, number_of_colors):
    add_or_subtract = 1 if np.random.random() < 0.5 else -1
    return (previous_color + add_or_subtract) % number_of_colors


def harmonic_mutation_step(previous_color, number_of_colors, array_mutation_strength):
    add_or_subtract = 1 if np.random.random() < 0.5 else -1
    random_value = np.random.random()
    cumulative_sum = 0
    for i, p in enumerate(array_mutation_strength):
        if random_value < cumulative_sum + p:
            return (previous_color + add_or_subtract * i) % number_of_colors
    return previous_color
