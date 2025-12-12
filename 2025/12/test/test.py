import unittest
from unittest.mock import patch
from src import solve

EXAMPLE = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

ANSWER1 = 2
ANSWER2 = 0


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, ANSWER1)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, ANSWER2)

    def test_parse_input(self):
        shapes, problems = solve.parse_input(EXAMPLE)
        expected_shapes = [
            ((1, 1, 1), (1, 1, 0), (1, 1, 0)),
            ((1, 1, 1), (1, 1, 0), (0, 1, 1)),
            ((0, 1, 1), (1, 1, 1), (1, 1, 0)),
            ((1, 1, 0), (1, 1, 1), (1, 1, 0)),
            ((1, 1, 1), (1, 0, 0), (1, 1, 1)),
            ((1, 1, 1), (0, 1, 0), (1, 1, 1)),
        ]
        expected_problems = [
            (((4, 4)), (0, 0, 0, 0, 2, 0)),
            (((12, 5)), (1, 0, 1, 0, 2, 2)),
            (((12, 5)), (1, 0, 1, 0, 3, 2)),
        ]
        self.assertEqual(shapes, expected_shapes)
        self.assertEqual(problems, expected_problems)
