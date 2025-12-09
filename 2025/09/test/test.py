import unittest
from unittest.mock import patch
from src import solve

EXAMPLE = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip().splitlines()

ANSWER1 = 50
ANSWER2 = 0


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, ANSWER1)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, ANSWER2)

    def test_expand_input(self):
        coords = solve.expand_input(EXAMPLE)
        expected_coords = [
            (7, 1),
            (11, 1),
            (11, 7),
            (9, 7),
            (9, 5),
            (2, 5),
            (2, 3),
            (7, 3),
        ]
        self.assertEqual(coords, expected_coords)

    def test_calculate_areas(self):
        coords = solve.expand_input(EXAMPLE)
        areas = solve.calculate_areas(coords)
        # Just test that we have the right number of areas calculated
        self.assertEqual(len(areas), 28)  # 8 choose 2 = 28
        case1 = next((x for x in areas if x[0] == 6))
        self.assertSequenceEqual(case1[1], (7, 3, 2, 3))
