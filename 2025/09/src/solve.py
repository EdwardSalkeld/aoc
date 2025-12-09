import itertools


def solve(part: int = 1) -> int:
    raw_input = read_input()
    coords = expand_input(raw_input)
    if part == 1:
        # areas = calculate_areas(list(coords))
        # largest_area = max(areas, key=lambda x: x[0])
        # return largest_area[0]
        return calculate_largest_area(list(coords), None, None)
    if part == 2:
        safe_space = calculate_safe_space(coords)
        x_to_keystones = calculate_vertices(safe_space)
        return calculate_largest_area(list(coords), safe_space, x_to_keystones)
    return 0


def expand_input(raw_input: list[str]) -> list[tuple[int, int]]:
    return [
        (int(x_str), int(y_str))
        for line in raw_input
        for x_str, y_str in [line.split(",")]
    ]


type Coordinate = tuple[int, int]
type Rectangle = tuple[int, int, int, int]  # x1, y1, x2, y2


def calculate_areas(coords: list[Coordinate]) -> list[tuple[int, Rectangle]]:
    areas = []
    while coords:
        coord = coords.pop()
        for other in coords:
            area = (abs(coord[0] - other[0]) + 1) * (abs(coord[1] - other[1]) + 1)
            areas.append((area, (coord[0], coord[1], other[0], other[1])))
    # for area in areas:
    #     print(f"Area: {area[0]}, Rectangle: {area[1]}")
    return areas


def calculate_largest_area(
    coords: list[Coordinate],
    safe_space: set[Coordinate],
    x_to_keystones: dict[int, list[int]] | None,
) -> int:
    largest_area = 0
    areas = []
    while coords:
        coord = coords.pop()
        for other in coords:
            area = (
                (abs(coord[0] - other[0]) + 1) * (abs(coord[1] - other[1]) + 1),
                coord,
                other,
            )
            areas.append(area)
    areas.sort(key=lambda x: x[0], reverse=True)

    if x_to_keystones is None:
        print("Not doing safety check")
        return areas[0][0]
    unsafe = set()
    for ix, area in enumerate(areas):
        if check_area_safe(area[1], area[2], safe_space, x_to_keystones, unsafe):
            largest_area = area[0]
            return largest_area
        print(
            f"{ix + 1}/{len(areas)} checked, largest safe area so far: {largest_area}"
        )
    return largest_area


def check_area_safe(
    first: Coordinate,
    second: Coordinate,
    safe_space: set[Coordinate],
    x_to_keystones: dict[int, list[int]],
    unsafe: set[Coordinate],
) -> bool:
    min_x = min(first[0], second[0])
    max_x = max(first[0], second[0])
    min_y = min(first[1], second[1])
    max_y = max(first[1], second[1])
    points_to_check = [(x, min_y) for x in range(min_x, max_x + 1)]
    points_to_check += [(x, max_y) for x in range(min_x, max_x + 1)]
    points_to_check += [(min_x, y) for y in range(min_y, max_y + 1)]
    points_to_check += [(max_x, y) for y in range(min_y, max_y + 1)]

    for x, y in points_to_check:
        keystones = x_to_keystones.get(x, [])
        if not keystones:
            print("No keystones at x={x}, area not safe.")
            return False
        if (x, y) in unsafe:
            return False
        if y not in keystones and (x, y) not in safe_space:
            one_side = [k for k in keystones if k >= y + 1]
            if len(one_side) % 2 == 0:
                # print(
                #     f"At ({x}, {y}), even number of keystones {keystones}:{one_side}, area not safe."
                # )
                unsafe.add((x, y))
                return False
            else:
                safe_space.add((x, y))
    # for x in range(min_x, max_x + 1):
    #     keystones = x_to_keystones.get(x, [])
    #     if not keystones:
    #         print("No keystones at x={x}, area not safe.")
    #         return False
    #     for y in range(min_y, max_y + 1):
    #         if y not in keystones and (x, y) not in safe_space:
    #             one_side = [k for k in keystones if k >= y + 1]
    #             if len(one_side) % 2 == 0:
    #                 # print(
    #                 #     f"At ({x}, {y}), even number of keystones {keystones}:{one_side}, area not safe."
    #                 # )
    #                 return False
    return True


def print_safe(safe_space: set[Coordinate]):
    x_to_keystones = calculate_vertices(safe_space)
    max_x = max(safe_space, key=lambda x: x[0])[0]
    max_y = max(safe_space, key=lambda x: x[1])[1]
    i = 0
    cols = [x % 10 for x in range(0, max_x + 1)]
    yield "".join(str(c) for c in cols)
    for y in range(0, max_y + 1):
        row = ""
        for x in range(0, max_x + 1):
            keystones = x_to_keystones.get(x, [])
            if (x, y) in safe_space:
                row += "#"
            elif len([k for k in keystones if k >= y]) % 2 == 1:
                row += "%"
            else:
                row += "."
        yield row
        i += 1
        if i % 1000 == 0:
            print(f"Printed {i} rows / {max_y}...")


def calculate_safe_space(coords: list[Coordinate]) -> set[Coordinate]:
    safe_space = set()
    coords = list(coords)
    coords.append(coords[0])
    for first, second in itertools.pairwise(coords):
        if first[0] == second[0]:
            x = first[0]
            for y in range(min(first[1], second[1]), max(first[1], second[1]) + 1):
                safe_space.add((x, y))
            if x == 97740:
                print(f"Adding a line along x from {first[1]} to {second[1]}")
        elif first[1] == second[1]:
            y = first[1]
            for x in range(min(first[0], second[0]), max(first[0], second[0]) + 1):
                safe_space.add((x, y))
                if x == 97740:
                    print(
                        f"Adding a line that crosses x=97740 at y={y}. First: {first}, Second: {second}"
                    )

        else:
            raise ValueError(
                f"Misundersood something. These aren't a row or column {first}, {second}"
            )
    return safe_space


def calculate_vertices(coords: set[Coordinate]):
    coords_by_x = {}
    for coord in coords:
        if coord[0] not in coords_by_x:
            coords_by_x[coord[0]] = []
        coords_by_x[coord[0]].append(coord[1])
    keystones_by_x = {}
    for x, ys in coords_by_x.items():
        debug = []
        ys.sort()
        current_range = None
        keystones = []
        for y in ys:
            if current_range is None:
                current_range = [y, y]
                keystones.append(current_range)
            elif current_range[1] + 1 == y:
                current_range[1] = y
            elif current_range[1] + 1 < y:
                current_range = [y, y]
                keystones.append(current_range)
            else:
                raise ValueError("Wrong order")
            # if current_run is None:
            #     keystones.add(y)
            # elif current_run + 1 < y:
            #     debug.append(f"Adding keystones at {current_run} and {y}")
            #     keystones.add(current_run)
            #     keystones.add(y)
            # elif current_run + 1 == y:
            #     pass
            # else:
            #     raise ValueError("Wrong order")
        # print(f"x={x}, keystones={keystones}")
        if len(keystones) % 2 == 0:
            keystones_by_x[x] = [k[0] for k in keystones]
        else:
            k_points = [k[0] for k in keystones if k[0] == k[1]]
            k_ranges = [(k[0], k[1]) for k in keystones if k[0] != k[1]]
            k_range_expansion = []
            for k_range in k_ranges:
                k_range_expansion.append(k_range[0])
                k_range_expansion.append(k_range[1])
            # print(
            #     f"Started with {len(keystones)}, {len(k_points)} points {len(k_ranges)} ranges"
            # )
            # print("Expanded ranges to:", len(k_range_expansion))
            k_points.extend(k_range_expansion)
            keystones_by_x[x] = sorted(k_points)

    return keystones_by_x


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 4739623064
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")  # 1654141440


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
