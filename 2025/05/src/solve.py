from typing import Self


class SafeRange:
    def __init__(self, start: int, end: int, next: Self | None) -> None:
        self.start = start
        self.end = end
        self.next = next

    def print(self) -> None:
        print(f"[{self.start}-{self.end}]")
        if self.next:
            self.next.print()

    def collect_length(self) -> int:
        length = self.end - self.start + 1
        # special dummy node at start!
        if self.end == 0:
            length = 0
        if self.next:
            length += self.next.collect_length()
        return length


def add_node(root: SafeRange, start: int, end: int) -> SafeRange:
    if start < root.start:
        # we're making a new root.
        safe_end = end
        safe_next = root.next
        if end >= root.start - 1:
            safe_end = max(end, root.end)
        else:
            safe_next = root
        return SafeRange(start, safe_end, safe_next)
    elif start >= root.start and start - 1 <= root.end:
        # overlapping range. we extend
        extend_node(root, end)
    elif root.next:
        # walk on down
        root.next = add_node(root.next, start, end)
    else:
        # add new node at end
        root.next = SafeRange(start, end, None)
    return root


def extend_node(node: SafeRange, end: int) -> None:
    while end > node.end:
        if node.next is None:
            # we update this one, there are no more
            node.end = end
        elif node.next.start - 1 > end:
            # we update this one, the next one is a new range
            node.end = end
        else:
            # we merge.
            node.end = node.next.end
            node.next = node.next.next


def add_range(tree: SafeRange | None, line: str):
    if line.isnumeric():
        start = end = int(line)
    else:
        start_s, end_s = line.split("-")
        start = int(start_s)
        end = int(end_s)
    if tree is None:
        return SafeRange(start, end, None)
    return add_node(tree, start, end)


def solve(part: int = 1) -> tuple[int, int]:
    raw_input = read_input()
    fresh_count = 0
    raw_lines = raw_input.strip().splitlines()

    tree_building = True
    tree = SafeRange(0, 0, None)
    for line in raw_lines:
        if tree_building:
            if line == "":
                tree_building = False
                continue
            tree = add_range(tree, line)
        else:
            value = int(line)
            if test_value(tree, value):
                fresh_count += 1
    return fresh_count, tree.collect_length()


def test_value(tree: SafeRange, value: int) -> bool:
    if value < tree.start:
        return False
    elif value <= tree.end:
        return True
    elif tree.next:
        return test_value(tree.next, value)
    return False


def main() -> None:
    part_one, part_two = solve()
    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


def read_input() -> str:
    with open("./input", "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
