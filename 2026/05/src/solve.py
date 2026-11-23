from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent / "input"


def solve(part: int = 1) -> int:
    lines = read_input()
    return 0


def main() -> None:
    print(f"Part One: {solve()}")
    print(f"Part Two: {solve(part=2)}")


def read_input() -> list[str]:
    return INPUT_PATH.read_text().strip().splitlines()


if __name__ == "__main__":
    main()
