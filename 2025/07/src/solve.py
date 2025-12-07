from typing import Self


class Beam:
    def __init__(self, col_ix: int, melge_val=1) -> None:
        self.col_ix = col_ix
        self.melge_val = melge_val
        self.continues = 0
        self.splits: list[Beam] = []

    def feed(self, row: str) -> list[Self]:
        if row[self.col_ix] == ".":
            self.continues += 1
            return [self]
        else:
            left = Beam(self.col_ix - 1, self.melge_val)
            right = Beam(self.col_ix + 1, self.melge_val)
            self.splits = [left, right]
            return [left, right]

    def collect_count(self) -> int:
        if self.splits:
            return 1 + sum([split.collect_count() for split in self.splits])
        else:
            return 0

    def collect_melge_val(self) -> int:
        if self.splits:
            return sum([split.collect_melge_val() for split in self.splits])
        else:
            return self.melge_val


def melge(beams: list[Beam]) -> list[Beam]:
    col_to_beams = {}
    for beam in beams:
        beams_at_col = col_to_beams.get(beam.col_ix, [])
        beams_at_col.append(beam)
        col_to_beams[beam.col_ix] = beams_at_col
    melged = []
    for beams_at_col in col_to_beams.values():
        beam = beams_at_col[0]
        beam.melge_val = sum([b.melge_val for b in beams_at_col])
        melged.append(beam)
        for other in beams_at_col[1:]:
            other.melge_val = 0
    return melged


def solve(part: int = 1) -> int:
    raw_input = read_input()
    first_line = raw_input.pop(0)
    beams: list[Beam] = []
    initial = Beam(first_line.index("S"))
    beams.append(initial)
    for line in raw_input:
        new_beams = []
        for beam in beams:
            new_beams.extend(beam.feed(line))
        beams = melge(new_beams)

        debug_line = list(line)
        for beam in beams:
            debug_line[beam.col_ix] = "|"
        print_ln = "".join(debug_line)
        print_ln += f" -> {initial.collect_count()}"
        print(print_ln)

    if part == 1:
        return initial.collect_count()
    if part == 2:
        return initial.collect_melge_val()
    return 0


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 1499
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")  # 24743903847942


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
