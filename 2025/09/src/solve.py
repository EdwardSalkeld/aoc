def solve(part: int = 1) -> int:
    raw_input = read_input()
    coords = expand_input(raw_input)
    areas = calculate_areas(coords)
    largest_area = max(areas, key=lambda x: x[0])
    if part == 1:
        return largest_area[0]
    return 0


def expand_input(raw_input: list[str]) -> list[tuple[int, int]]:
    return [
        (int(x_str), int(y_str))
        for line in raw_input
        for x_str, y_str in [line.split(",")]
    ]


type Coordinate = tuple[int, int]
type Rectangle = tuple[int, int, int, int]  # x1, y1, x2, y2


def calculate_areas(
    coords: list[Coordinate],
) -> list[tuple[int, Rectangle]]:
    areas = []
    while coords:
        coord = coords.pop()
        for other in coords:
            area = (abs(coord[0] - other[0]) + 1) * (abs(coord[1] - other[1]) + 1)
            areas.append((area, (coord[0], coord[1], other[0], other[1])))
    # for area in areas:
    #     print(f"Area: {area[0]}, Rectangle: {area[1]}")
    return areas


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 4739623064
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
