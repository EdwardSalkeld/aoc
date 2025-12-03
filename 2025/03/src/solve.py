def solve(part: int = 1) -> int:
    raw_input = read_input()
    if part == 1:
        return sum([calculate_joltage(x) for x in raw_input])
    answer = 0
    return 0


def calculate_joltage(line: str) -> int:
    first_number_candidates = list(line[:-1])
    first = max(first_number_candidates)
    first_ix = first_number_candidates.index(first)
    second_number_candidates = list(line[first_ix + 1 :])
    second = max(second_number_candidates)
    return 10 * int(first) + int(second)


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().split()


if __name__ == "__main__":
    main()
