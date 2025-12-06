import unittest
from unittest.mock import patch
from src import solve

EXAMPLE = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

ANSWER1 = 4277556
ANSWER2 = 3263827


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE.strip().splitlines())
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, ANSWER1)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, ANSWER2)
