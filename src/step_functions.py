import numpy as np

UNIFORM_MUTATION = "uniform_mutation"
UNIT_MUTATION = "unit_mutation"
HARMONIC_MUTATION = "harmonic_mutation"


class StepFactory:
    def uniform_mutation_step(self, previous_color):
        return (previous_color + np.random.randint(1, self.number_of_colors)) % self.number_of_colors

    
    def unit_mutation_step(self, previous_color):
        add_or_subtract = 1 if np.random.random() < 0.5 else -1
        return (previous_color + add_or_subtract) % self.number_of_colors


    def harmonic_mutation_step(self, previous_color):
        add_or_subtract = 1 if np.random.random() < 0.5 else -1
        random_value = np.random.random()
        l, r = 0, self.number_of_colors - 1
        # [l, r)
        while l < r - 1:
            m = (l + r) // 2
            if self.cumulative[m] <= random_value:
                l = m
            else:
                r = m
        return (previous_color + l + 1) % self.number_of_colors

    def __init__(self, number_of_colors, step_name):
        self.step_name = step_name
        self.number_of_colors = number_of_colors
        if step_name == UNIFORM_MUTATION:
            self.step_function = self.uniform_mutation_step
        elif step_name == UNIT_MUTATION:
            self.step_function = self.unit_mutation_step
        elif step_name == HARMONIC_MUTATION:
            self.step_function = self.harmonic_mutation_step
            self.cumulative = [0] * number_of_colors
            harmonic = 0
            for i in range(1, number_of_colors):
                harmonic += 1 / i
            for i in range(1, number_of_colors):
                self.cumulative[i] = self.cumulative[i - 1] + 1 / i / harmonic
        else:
            self.step_function = Exception



