def solve(part: int = 1) -> int:
    raw_input = read_input()
    arr_input = process_input(raw_input)
    if part == 1:
        pass
        return solve_part_one(arr_input)
    answer = 0
    return 0


def process_input(raw_input: list[str]) -> list[list[int]]:
    matrix = []
    for line in raw_input:
        line = line.strip()
        row = [1 if x == "@" else 0 for x in line]
        matrix.append(row)
    return matrix


def solve_part_one(arr: list[list[int]]) -> int:
    answer = 0
    pretty = "\n"
    neigghbor_counts = count_neightbors(arr)
    for markers, counts in zip(arr, neigghbor_counts):
        for marker, count in zip(markers, counts):
            available = (marker == 1) and (count < 4)
            if available:
                answer += 1
                pretty += "x"
            elif marker == 1:
                pretty += "@"
            else:
                pretty += "."
        pretty += "\n"

    print(pretty)
    return answer


def count_neightbors(arr: list[list[int]]) -> list[list[int]]:
    max_y = len(arr) - 1
    max_x = len(arr[0]) - 1
    counters = [[0 for x in row] for row in arr]
    for y, row in enumerate(arr):
        for x, col in enumerate(row):
            # if I am an object, increment all subsequent cells
            if col == 1:
                if x < max_x:
                    counters[y][x + 1] += 1  # right
                if x > 0:
                    counters[y][x - 1] += 1  # left
                if y < max_y:
                    next_row = counters[y + 1]
                    next_row[x] += 1  # down
                    if x > 0:
                        next_row[x - 1] += 1  # down-left
                    if x < max_x:
                        next_row[x + 1] += 1  # down-right:w
                if y > 0:
                    prev_row = counters[y - 1]
                    try:
                        prev_row[x] += 1  # down
                    except IndexError:
                        print(f"X={x} Y={y} prev row = {prev_row}, x={x}")
                        raise
                    if x > 0:
                        prev_row[x - 1] += 1  # down-left
                    if x < max_x:
                        prev_row[x + 1] += 1  # down-right:w
    return counters
    # # corners are always fine
    # corners = sum([arr[0][0], arr[0][max_y], arr[max_x][0], arr[max_x][max_y]])
    #
    # # edges need sweeping
    # return 0


def main() -> None:
    part_one = solve()
    print(f"Part One: {part_one}")
    part_two = solve(part=2)
    print(f"Part Two: {part_two}")


def read_input() -> list[str]:
    with open("./input", "r") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    main()
