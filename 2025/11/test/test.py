import unittest
from unittest.mock import patch
from src import solve

EXAMPLE = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip().splitlines()

EXAMPLE2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip().splitlines()
ANSWER1 = 5
ANSWER2 = 2


class TestExample(unittest.TestCase):
    @patch("src.solve.read_input", return_value=EXAMPLE)
    def test_final_answer(self, _mock):
        answer = solve.solve()
        self.assertEqual(answer, ANSWER1)

    @patch("src.solve.read_input", return_value=EXAMPLE2)
    def test_final_answer_part2(self, _mock):
        answer_part2 = solve.solve(part=2)
        self.assertEqual(answer_part2, ANSWER2)

    def test_build_node_lookups(self):
        lookups = solve.build_node_lookups(EXAMPLE)
        self.assertEqual(lookups["hhh"], ["ccc", "fff", "iii"])

    def test_walk_graph(self):
        lookups = solve.build_node_lookups(EXAMPLE)
        paths = set()
        solve.walk_graph(lookups, ["you"], paths)
        self.assertEqual(len(paths), 5)

    # def test_walk_graph_2(self):
    #     lookups = solve.build_node_lookups(EXAMPLE2)
    #     paths = set()
    #     solve.walk_graph_2(lookups, ["svr"], paths)
    #     self.assertEqual(len(paths), 2)
