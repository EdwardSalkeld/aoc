import unittest
import math
from unittest.mock import patch
from src import solve

EXAMPLE = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip().splitlines()

ANSWER1 = 40
ANSWER2 = 25272


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        answer = solve.solve(connections=10)
        self.assertEqual(answer, ANSWER1)
        answer_part2 = solve.solve(part=2, connections=10)
        self.assertEqual(answer_part2, ANSWER2)

    def test_expand_input(self):
        text = """
        1,2,3
        4,5,6
        7,8,9
        """.strip().splitlines()
        expected = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
        ]
        result = solve.expand_input(text)
        self.assertEqual(result, expected)

    def test_calculate_distances(self):
        boxes = [
            (0, 0, 0),
            (3, 4, 0),
            (0, 8, 6),
        ]
        result = solve.calculate_distances(boxes)
        expected_distances = {
            5.0: ((3, 4, 0), (0, 0, 0)),
            10.0: ((0, 8, 6), (0, 0, 0)),
            math.sqrt(61): ((0, 8, 6), (3, 4, 0)),
        }
        print(f"{result}")
        for dist in expected_distances:
            print("Checking distance:", dist)

            self.assertIn(dist, result)
            self.assertEqual(result[dist], expected_distances[dist])
