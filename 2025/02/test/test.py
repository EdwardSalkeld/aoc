import unittest
from unittest.mock import patch
from src import solve


class TestExample(unittest.TestCase):
    def test_expand_input(self):
        raw_input = "1,2,5-7,10"
        expected_output = [1, 2, 5, 6, 7, 10]
        self.assertEqual(solve.expand_input(raw_input), expected_output)

    def test_check_item_valid(self):
        all_valid = [101, 121, 123456789, 1234123]
        for item in all_valid:
            self.assertTrue(solve.check_item(item), f"Item {item} should be valid")
        all_invalid = [11, 122, 123123, 12345123456, 123434, 123456788, 12345678891]
        for item in all_invalid:
            self.assertFalse(solve.check_item(item), f"Item {item} should be invalid")

    @patch("src.solve.read_input", return_value="1,9-12,20,22,1000")
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, 11 + 22 + 1000)
