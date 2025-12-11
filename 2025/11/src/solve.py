def solve(part: int = 1) -> int:
    raw_input = read_input()
    node_lookups = build_node_lookups(raw_input)
    if part == 1:
        paths = set()
        walk_graph(node_lookups, ["you"], paths)
        answer = len(paths)
        return answer
    answer = 0
    return 0


def walk_graph(
    node_lookups: dict[str, list[str]], current_path: list[str], paths: set[str]
) -> int:
    start_node = current_path[-1]
    node_connections = node_lookups[start_node]
    for connection in node_connections:
        if connection == "out":
            path_str = ",".join(current_path + [connection])
            # print(f"Found path: {path_str}")
            paths.add(path_str)
        else:
            walk_graph(node_lookups, current_path + [connection], paths)


def build_node_lookups(raw_input: list[str]) -> dict[str, list[str]]:
    lookups = {}
    for line in raw_input:
        parts = line.split(": ")
        node = parts[0]
        connections = parts[1].split(" ")
        lookups[node] = connections
    return lookups


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 423
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
