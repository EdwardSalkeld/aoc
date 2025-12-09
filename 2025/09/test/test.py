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
ANSWER2 = 24


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

    def test_safe_space(self):
        coords = solve.expand_input(EXAMPLE)
        safe_space = solve.calculate_safe_space(coords)
        # Just test that we have some safe space calculated
        self.assertGreater(len(safe_space), 0)
        self.assertIn((6, 3), safe_space)
        rows = solve.print_safe(safe_space)
        print("\n")
        for row in rows:
            print(row)
        self.assertTrue((7, 2) in safe_space)

    def test_safe_space2(self):
        input_data = [
            (1, 0),
            (3, 0),
            (3, 3),
            (5, 3),
            (5, 0),
            (7, 0),
            (7, 5),
            (1, 5),
        ]
        safe_space = solve.calculate_safe_space(input_data)
        # Just test that we have some safe space calculated
        self.assertGreater(len(safe_space), 0)
        rows = solve.print_safe(safe_space)
        print("\n")
        for row in rows:
            print(row)
        self.assertTrue((7, 2) in safe_space)

    def test_safe_space3(self):
        input_data = [
            (0, 1),
            (0, 3),
            (3, 3),
            (3, 5),
            (0, 5),
            (0, 7),
            (5, 7),
            (5, 1),
        ]
        safe_space = solve.calculate_safe_space(input_data)
        # Just test that we have some safe space calculated
        self.assertGreater(len(safe_space), 0)
        rows = solve.print_safe(safe_space)
        print("\n")
        for row in rows:
            print(row)

    def test_calculate_vertices(self):
        ys = [1, 4]
        r = solve.calculate_vertices({(2, y) for y in ys})
        self.assertEqual(r, {2: [1, 4]})

        ys = [1, 3, 4, 5, 7]
        r = solve.calculate_vertices({(2, y) for y in ys})
        self.assertEqual(r, {2: [1, 3, 5, 7]})

        ys = [0, 3, 4, 5]
        r = solve.calculate_vertices({(2, y) for y in ys})
        self.assertEqual(r, {2: [0, 3]})
