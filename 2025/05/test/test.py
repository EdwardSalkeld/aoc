import unittest
from unittest.mock import patch
from src import solve

EXAMPLE_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

EXAMPLE_ANSWER = 3


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE_INPUT)
    def test_final_answer(self, _mock):
        answer1, answer2 = solve.solve()
        self.assertEqual(answer1, EXAMPLE_ANSWER)
        self.assertEqual(answer2, 14)

    def test_contiguous_ranges_merge(self):
        n = solve.SafeRange(0, 0, None)
        n = solve.add_node(n, 10, 19)
        n = solve.add_node(n, 20, 29)
        n = solve.add_node(n, 30, 39)
        self.assertEqual(n.next.start, 10)
        self.assertEqual(n.next.end, 39)

    def test_contiguous_ranges_merge_any_order(self):
        # in any order
        n = solve.SafeRange(0, 0, None)
        n = solve.add_node(n, 20, 29)
        n = solve.add_node(n, 40, 49)
        n = solve.add_node(n, 30, 39)
        n = solve.add_node(n, 10, 19)
        n.print()
        self.assertEqual(n.next.start, 10)
        self.assertEqual(n.next.end, 49)

    def test_collect_length(self):
        n = solve.SafeRange(0, 0, None)
        n = solve.add_node(n, 10, 19)
        n = solve.add_node(n, 30, 39)
        n = solve.add_node(n, 50, 59)
        self.assertEqual(n.collect_length(), 30)

    def test_matching_starts(self):
        n = solve.SafeRange(0, 0, None)
        n = solve.add_node(n, 10, 19)
        n = solve.add_node(n, 30, 39)
        n = solve.add_node(n, 50, 59)
        n = solve.add_node(n, 30, 44)
        self.assertEqual(n.collect_length(), 35)
