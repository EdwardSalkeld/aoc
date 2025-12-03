import unittest
from unittest.mock import patch
from src import solve


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value="1,9-12,20,22,1010, 462149")
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, 0)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, 0)
