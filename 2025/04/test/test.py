import unittest
from unittest.mock import patch
from src import solve

EXAMPLE_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

EXAMPLE_OUTPUT_1 = """
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""

EXAMPLE_ANSWER = sum([1 for x in EXAMPLE_OUTPUT_1 if x == "x"])


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE_INPUT.strip().splitlines())
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, EXAMPLE_ANSWER)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, 43)
        answer = solve.solve(optimised=True)
        self.assertEqual(answer, EXAMPLE_ANSWER)
        answer_part2 = solve.solve(part=2, optimised=True)
        self.assertEqual(answer_part2, 43)

    def test_process_input(self):
        test_in = """
        ..@@
        .@..
        @...
        """
        expected_out = [
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ]
        self.assertEqual(
            solve.process_input(test_in.strip().splitlines()), expected_out
        )

    def test_count_neighbours(self):
        test_in = [
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 0],
        ]
        test_out = [
            [1, 2, 2, 1],
            [3, 4, 5, 3],
            [2, 3, 2, 1],
        ]
        solved = solve.count_neightbors(test_in)
        self.assertEqual(solved, test_out)
        solved = solve.alt_count_neightbors(test_in)
        self.assertEqual(solved, test_out)

    def test_solve_part_one(self):
        test_in = [
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 0],
        ]
        solved = solve.solve_part_one(test_in)
        self.assertEqual(solved, 5)
