def solve(part: int = 1) -> int:
    raw_input = read_input()
    if part == 1:
        return sum([calculate_joltage(x) for x in raw_input])
    if part == 2:
        return sum([calculate_joltage_variable(x, 12) for x in raw_input])
    return 0


def calculate_joltage(line: str) -> int:
    first_number_candidates = line[:-1]
    first = max(first_number_candidates)
    first_ix = first_number_candidates.index(first)
    second_number_candidates = line[first_ix + 1 :]
    second = max(second_number_candidates)
    return 10 * int(first) + int(second)


def calculate_joltage_variable(line: str, required: int) -> int:
    joltages = []
    start_ix = 0
    while required > 0:
        required -= 1
        if required == 0:
            candidates = line[start_ix:]
        else:
            candidates = line[start_ix:-required]
        # print(f"L {line} C {candidates} F {start_ix} E {-required}")
        selected = max(candidates)
        start_ix += candidates.index(selected) + 1
        multiplier = 10 ** (required)
        joltages.append(int(selected) * multiplier)
    return sum(joltages)


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
