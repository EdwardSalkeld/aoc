import unittest
from pathlib import Path
from unittest.mock import patch

from src import solve

DAY_DIR = Path(__file__).parent.parent


def read(name: str) -> str | None:
    path = DAY_DIR / name
    return path.read_text().strip() if path.exists() else None


class TestExample(unittest.TestCase):
    def check_part(self, part: int) -> None:
        answer = read(f"answer{part}")
        if not answer:
            self.skipTest(f"no answer{part} yet")
        # Some puzzles give part 2 its own example.
        example = read(f"example{part}") or read("example") or ""
        with patch("src.solve.read_input", return_value=example.splitlines()):
            self.assertEqual(str(solve.solve(part=part)), answer)

    def test_part1(self):
        self.check_part(1)

    def test_part2(self):
        self.check_part(2)
