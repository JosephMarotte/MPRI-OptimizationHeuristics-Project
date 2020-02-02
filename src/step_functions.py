import numpy as np

UNIFORM_COLOR = "uniform_color"
ADJACENT_COLOR = "adjacent_color"
RANDOM_COLOR_WITH_MUTATION_STRENGTH = "random_color_with_mutation_strength"


class StepFactory:
    @staticmethod
    def build_step(number_of_colors, step_name, array_mutation_strength):
        if step_name == UNIFORM_COLOR:
            return lambda x: pick_new_color_uniformly(x, number_of_colors)
        elif step_name == ADJACENT_COLOR:
            return lambda x: random_adjacent_color(x, number_of_colors)
        elif step_name == RANDOM_COLOR_WITH_MUTATION_STRENGTH:
            return lambda x: random_color_with_mutation_strength(x, number_of_colors, array_mutation_strength)
        else:
            raise Exception


def pick_new_color_uniformly(previous_color, number_of_colors):
    return previous_color + np.random.randint(1, number_of_colors - 1)


def random_adjacent_color(previous_color, number_of_colors):
    add_or_subtract = 1 if np.random.random() < 0.5 else -1
    return (previous_color + add_or_subtract) % number_of_colors


def random_color_with_mutation_strength(previous_color, number_of_colors, array_mutation_strength):
    add_or_subtract = 1 if np.random.random() < 0.5 else -1
    random_value = np.random.random()
    cumulative_sum = 0
    for i, p in enumerate(array_mutation_strength):
        if random_value < cumulative_sum + p:
            return (previous_color + add_or_subtract * i) % number_of_colors
    return previous_color
