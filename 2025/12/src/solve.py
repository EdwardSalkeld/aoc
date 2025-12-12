def solve(part: int = 1) -> int:
    raw_input = read_input()
    shapes, problems = parse_input(raw_input)
    if part == 1:
        answer = 0
        for problem in problems:
            area, shape_counts = problem
            # print(f"Area {area[0]}x{area[1]} = {area[0] * area[1]}")
            total_shape_area = 0
            for shape_index, count in enumerate(shape_counts):
                shape = shapes[shape_index]
                shape_area = sum([sum(x) for x in shape])
                # print(
                #     f"shape[{shape_index}] A={shape_area} * {count} = {shape_area * count}"
                # )
                total_shape_area += shape_area * count
            print(f"Total shape area = {total_shape_area}")
            if total_shape_area > area[0] * area[1]:
                print("  OVERFLOW")
            else:
                answer += 1
        print(f"Naive answer {answer}/{len(problems)}")
        return answer

    answer = 0
    return 0


type Shape = tuple[tuple[int]]
type Area = tuple[int, int]
type Problem = tuple[Area, tuple[int]]


def parse_input(raw_input: str) -> tuple[list[Shape], list[Problem]]:
    it = iter(raw_input.splitlines())
    shapes = []
    problems = []
    try:
        while True:
            line = next(it).strip()
            if line == f"{len(shapes)}:":
                shape_rows = []
                for i in range(3):
                    shape_line = next(it)
                    shape_row = tuple(1 if c == "#" else 0 for c in shape_line.strip())
                    shape_rows.append(shape_row)
                shapes.append(tuple(shape_rows))
            elif len(line) == 0:
                pass
            else:
                area_part = line.split(":")
                area_size = area_part[0].strip()
                width, height = map(int, area_size.split("x"))
                shape_counts = tuple(map(int, area_part[1].strip().split()))
                problems.append(((width, height), shape_counts))

    except StopIteration:
        pass

    return shapes, problems


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")  # 440. (oh boy I did not expect that to work!)
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> str:
    with open("./input", "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
