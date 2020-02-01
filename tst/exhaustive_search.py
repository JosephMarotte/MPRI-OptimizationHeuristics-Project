import unittest
import numpy as np
from src.exhaustive_search import exhaustive_search
from baseconvert import base

MAX_NUMBER_OF_ITER = 100_000
MAX_NUMBER_OF_COLORS = 10


class ExhaustiveSearchTst(unittest.TestCase):
    def test_exhaustive_search(self):
        number_of_colors = np.random.randint(2, MAX_NUMBER_OF_COLORS)
        disposition_in_base_10 = np.random.randint(100_000)
        disposition_to_guess = list(base(disposition_in_base_10, 10, number_of_colors))[::-1]
        number_of_call_needed = exhaustive_search(len(disposition_to_guess), number_of_colors, disposition_to_guess)
        self.assertEqual(disposition_in_base_10 + 1, number_of_call_needed)
