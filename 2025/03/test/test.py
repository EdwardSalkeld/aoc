import unittest
from unittest.mock import patch
from src import solve

EXAMPLE_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE_INPUT.strip().split("\n"))
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, 357)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, 3121910778619)

    def test_calculate_joltage(self):
        self.assertEqual(solve.calculate_joltage("987654321111111"), 98)
        self.assertEqual(solve.calculate_joltage("811111111111119"), 89)
        self.assertEqual(solve.calculate_joltage("234234234234278"), 78)
        self.assertEqual(solve.calculate_joltage("818181911112111"), 92)

    def test_calculate_joltage_12(self):
        self.assertEqual(
            solve.calculate_joltage_variable("987654321111111", 12), 987654321111
        )
        self.assertEqual(
            solve.calculate_joltage_variable("811111111111119", 12), 811111111119
        )
        self.assertEqual(
            solve.calculate_joltage_variable("234234234234278", 12), 434234234278
        )
        self.assertEqual(
            solve.calculate_joltage_variable("818181911112111", 12), 888911112111
        )
