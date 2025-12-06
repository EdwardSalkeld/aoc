from typing import Generator

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def solve(part: int = 1) -> int:
    raw_input = read_input()
    answer = 0
    for problem in read_vertical(raw_input, part):
        log.debug(f"Raw: {problem}")
        operand = problem.pop()
        puzzle_str = f" {operand} ".join(problem)
        log.debug(f"Processed: {puzzle_str}")
        problem_result = eval(puzzle_str)
        log.debug(f"Result: {problem_result}")

        answer += problem_result
    return answer


def read_vertical(rows: list[str], part: int) -> Generator[list[str], None, None]:
    if part == 1:
        rows = [row.split() for row in rows]
        while len(rows[0]) > 0:
            yield ([row.pop() for row in rows])
    else:
        log.debug(f"Raw rows: {rows}")
        operands = rows.pop().split()
        log.debug(f"Operands: {operands}")
        rows = [list(row) for row in rows]
        log.debug(f"Processed rows: {rows}")

        puzzle_components = []
        while len(rows[0]) > 0:
            digits = [row.pop() for row in rows]
            log.debug(f"Digits: {digits}")
            if all([digit.isspace() for digit in digits]):
                puzzle_components.append(operands.pop())
                yield puzzle_components
                puzzle_components = []
            else:
                puzzle_components.append("".join(digits))
        puzzle_components.append(operands.pop())
        yield puzzle_components


def main() -> None:
    part_one = solve()
    log.info(f"Part One: {part_one}")  # 6295830249262
    part_two = solve(part=2)
    log.info(f"Part Two: {part_two}")  # 9194682052782


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    log.setLevel(logging.INFO)
    main()
