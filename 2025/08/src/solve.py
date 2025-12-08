import math


def solve(part: int = 1, connections=1000) -> int:
    raw_input = read_input()
    boxes = expand_input(raw_input)
    box_count = len(boxes)
    distance_matrix = calculate_distances(list(boxes))
    connection_sets, final_pair = create_links(
        distance_matrix, connections, box_count, part
    )
    if part == 1:
        group_count, group_coverage, product = count_groups(connection_sets)
        print(f"groups = {group_count} + ({len(boxes)} - {group_coverage})")
        return product
    if part == 2:
        print(f"Final pair was {final_pair}")
        print(f"X prod = {final_pair[0][0] * final_pair[1][0]}")
        return final_pair[0][0] * final_pair[1][0]
    return 0


def calculate_distances(
    boxes: list[tuple[int, int, int]],
) -> dict[float, tuple[int, int, int]]:
    distance_map = {}
    while boxes:
        box = boxes.pop()
        # print(f"Handling {box}")
        for other in boxes:
            distance = math.dist(box, other)
            if distance in distance_map:
                raise ValueError("Duplicate distance found")
            distance_map[distance] = (box, other)
            # print(f"Between {box} and {other} is {distance}")
    print(f"Calculated {len(distance_map)} distances")
    return distance_map


def create_links(
    distance_map: dict[float, tuple[int, int, int]],
    connections: int,
    box_count: int,
    part: int,
):
    connection_sets = {}
    distances = sorted(distance_map.keys())
    connections_made = 0
    checked = 0
    fns = {
        1: lambda _: connections_made < connections,
        2: lambda _: not connection_sets
        or len(next(iter(connection_sets.values()))) < box_count,
    }
    fn = fns[part]
    if not fn:
        raise ValueError("Invalid part")
    pair = None
    while fn(1):
        pair = distance_map[distances[checked]]
        checked += 1
        if pair[0] not in connection_sets and pair[1] not in connection_sets:
            # neither are connected. easy. add both ways
            connection_sets[pair[0]] = set()
            connection_sets[pair[1]] = connection_sets[pair[0]]
        elif pair[0] not in connection_sets:
            # one not connected. use other's
            connection_sets[pair[0]] = connection_sets[pair[1]]
        elif pair[1] not in connection_sets:
            # same, but other way round
            connection_sets[pair[1]] = connection_sets[pair[0]]
        elif pair[1] in connection_sets[pair[0]]:
            # these two are already connected. move along
            # print("Already connected (but not skipping):", pair)
            pass
        else:
            # both connected, but not to each other. need to merge sets
            # print("Merge!")
            set_to_merge = connection_sets[pair[1]]
            for item in set_to_merge:
                connection_sets[item] = connection_sets[pair[0]]
            connection_sets[pair[0]].update(set_to_merge)
        connection_sets[pair[0]].add(pair[0])
        connection_sets[pair[0]].add(pair[1])
        # print(f"Linking {pair[0]} and {pair[1]}")
        connections_made += 1

    return connection_sets, pair


def count_groups(
    connection_sets: dict[tuple[int, int, int], set],
) -> tuple[int, int, int]:
    all_groups = set([frozenset(x) for x in connection_sets.values()])
    group_count = len(all_groups)
    group_coverage = sum(len(g) for g in all_groups)
    print(f"Lens of all groups: {[len(g) for g in all_groups]}")
    print(f"Found {group_count} groups covering {group_coverage} boxes")
    largest_three_groups = sorted([len(g) for g in all_groups])[-3:]
    print(f"Largest three groups: {largest_three_groups}")
    product = (
        largest_three_groups[0] * largest_three_groups[1] * largest_three_groups[2]
    )
    print(f"Product of largest three groups: {product}")
    return group_count, group_coverage, product


def expand_input(raw_input: list[str]) -> list[tuple[int, int, int]]:
    boxes = []
    for line in raw_input:
        x, y, z = map(int, line.split(","))
        boxes.append((x, y, z))
    return boxes


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 68112
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")  # 44543856


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
