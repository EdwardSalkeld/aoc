from typing import Generator

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def solve(part: int = 1) -> int:
    raw_input = read_input()
    if part == 1:
        answer = 0
        for problem in read_vertical(raw_input):
            log.debug(f"Raw: {problem}")
            operand = problem.pop()
            puzzle_str = f" {operand} ".join(problem)
            log.debug(f"Processed: {puzzle_str}")
            problem_result = eval(puzzle_str)
            log.debug(f"Result: {problem_result}")

            answer += problem_result
        return answer
    return 0


def read_vertical(rows: list[str]) -> Generator[list[str], None, None]:
    rows = [row.split() for row in rows]
    while len(rows[0]) > 0:
        yield ([row.pop() for row in rows])


def main() -> None:
    part_one = solve()
    log.info(f"Part One: {part_one}")
    part_two = solve(part=2)
    log.info(f"Part Two: {part_two}")


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    log.setLevel(logging.INFO)
    main()
