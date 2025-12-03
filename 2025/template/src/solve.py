def solve(part: int = 1) -> int:
    raw_input = read_input()
    answer = 0
    return 0


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> str:
    with open("./input", "r") as f:
        return f.readline()


if __name__ == "__main__":
    main()
