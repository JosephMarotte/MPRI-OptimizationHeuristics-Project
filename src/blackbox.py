import numpy as np
from src.utils import generate_random_disposition


class BlackBox:
    number_of_call_made = None
    disposition = None
    array_size = None
    number_of_colors = None
    max_possible_evaluation = None

    def __init__(self, array_size, number_of_colors):
        self.array_size = array_size
        self.number_of_colors = number_of_colors
        self.max_possible_evaluation = array_size

    def new_session(self, disposition=None):
        self.number_of_call_made = 0
        if disposition is None:
            disposition = generate_random_disposition(self.array_size, self.number_of_colors)
        self.disposition = disposition

    def evaluate(self, disposition_guess):
        self.number_of_call_made += 1
        assert (len(disposition_guess) == len(self.disposition))
        return np.count_nonzero(disposition_guess == self.disposition)
