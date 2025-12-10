import unittest
from unittest.mock import patch
from src import solve

EXAMPLE = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip().splitlines()

ANSWER1 = 7
ANSWER2 = 0


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, ANSWER1)
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, ANSWER2)

    def test_expand_input(self):
        machines = solve.expand_input(EXAMPLE)
        self.assertEqual(len(machines), 3)
        self.assertEqual(machines[0].target_state, 0b0110)
        self.assertEqual(machines[1].target_state, 0b1000)
        self.assertEqual(machines[2].target_state, 0b101110)

        self.assertEqual(
            machines[0].operations, [0b1000, 0b1010, 0b0100, 0b1100, 0b101, 0b11]
        )

    def test_try_operations(self):
        machines = solve.expand_input(EXAMPLE)
        r1 = solve.solve_machine(machines[0])
        self.assertEqual(r1, 2)
        r2 = solve.solve_machine(machines[1])
        self.assertEqual(r2, 3)
        r3 = solve.solve_machine(machines[2])
        self.assertEqual(r3, 2)
