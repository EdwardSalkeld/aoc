import unittest
from unittest.mock import patch

from src import solve

EXAMPLE = """

""".strip().splitlines()

ANSWER1 = 0
ANSWER2 = 0


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        self.assertEqual(solve.solve(), ANSWER1)
        self.assertEqual(solve.solve(part=2), ANSWER2)
