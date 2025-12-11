def solve(part: int = 1) -> int:
    raw_input = read_input()
    node_lookups = build_node_lookups(raw_input)
    if part == 1:
        paths = set()
        walk_graph(node_lookups, ["you"], paths)
        answer = len(paths)
        return answer
    if part == 2:
        node_count = len(node_lookups)
        eligible_from_dac_to_out = set()
        walk_graph_collect_eligible(
            node_lookups, ["dac"], eligible_from_dac_to_out, set(), target="out"
        )
        print(f"Eligible from dac to out: {len(eligible_from_dac_to_out)}/{node_count}")
        # 57 nodes...

        eligible_from_dac_to_fft = set()
        walk_graph_collect_eligible(
            node_lookups, ["dac"], eligible_from_dac_to_fft, set(), target="fft"
        )
        print(f"Eligible from dac to fft: {len(eligible_from_dac_to_fft)}/{node_count}")
        # 0. Very interesting.

        eligible_from_svr_to_fft = set()
        walk_graph_collect_eligible(
            node_lookups,
            ["svr"],
            eligible_from_svr_to_fft,
            set(),
            target="fft",
        )
        # magic knowledge from above: the only route is src->fft->dac->out

        set1 = set()
        set2 = set()
        set3 = set()
        walk_graph2(node_lookups, ["svr"], set1, set(), set(), target="fft")
        walk_graph2(node_lookups, ["fft"], set2, set(), set(), target="dac")
        walk_graph2(node_lookups, ["dac"], set3, set(), set(), target="out")
        print(f"Set lens: {len(set1)} {len(set2)} {len(set3)}")

        return len(set1) * len(set2) * len(set3)
    return 0


def walk_graph(
    node_lookups: dict[str, list[str]],
    current_path: list[str],
    paths: set[str],
    target="out",
):
    start_node = current_path[-1]
    node_connections = node_lookups.get(start_node)
    if node_connections is None:
        return
    for connection in node_connections:
        if connection == target:
            path_str = ",".join(current_path + [connection])
            # print(f"Found path: {path_str}")
            paths.add(path_str)
        else:
            walk_graph(node_lookups, current_path + [connection], paths, target=target)


def walk_graph2(
    node_lookups: dict[str, list[str]],
    current_path: list[str],
    paths: set[str],
    path_nodes: set[str],
    bad_nodes: set[str],
    target: str,
):
    start_node = current_path[-1]
    node_connections = node_lookups.get(start_node)
    if node_connections is None:
        return
    for connection in node_connections:
        if connection in bad_nodes:
            continue
        if connection == target:
            path_str = ",".join(current_path + [connection])
            # print(f"Found path: {path_str}")
            paths.add(path_str)
            path_nodes.update(current_path)
        else:
            walk_graph2(
                node_lookups,
                current_path + [connection],
                paths,
                path_nodes,
                bad_nodes,
                target=target,
            )
    if start_node not in path_nodes:
        bad_nodes.add(start_node)
    # print(f"GOOD: {len(path_nodes)} BAD: {len(bad_nodes)}")


def walk_graph_collect_eligible(
    node_lookups: dict[str, list[str]],
    current_path: list[str],
    eligible: set[str],
    ineligible: set[str],
    target="out",
    depth=0,
):
    # print(f"T {target} D {depth} C {current_path[-1]} E {len(eligible)}")
    start_node = current_path[-1]
    node_connections = node_lookups[start_node]
    for connection in node_connections:
        if connection in eligible:
            continue  # this one can make it out. ignore
        if connection in ineligible:
            continue  # this one is blocked. ignore
        if connection == target:
            eligible.update(current_path)
        elif connection == "out":
            continue  # skip out if its not the target
        else:
            walk_graph_collect_eligible(
                node_lookups,
                current_path + [connection],
                eligible,
                ineligible,
                target=target,
                depth=depth + 1,
            )
    am_eligible = start_node in eligible
    # print(f"END C {current_path[-1]} Am eligible: {am_eligible}")
    if not am_eligible:
        ineligible.add(start_node)


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
    print(f"Part Two: {part_two}")  # 333657640517376


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
