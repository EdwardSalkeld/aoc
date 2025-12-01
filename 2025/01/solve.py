def part_one():
    cur = 50
    passed_by_zero = 0
    zeroes_seen = 0

    with open("input") as f:
        for line in f:
            initial = cur
            direction = -1 if line[0] == "L" else 1
            distance = int(line[1:].strip())

            passed_by_zero += abs(int(distance / 100))  # complete loops
            distance = distance % 100
            cur += direction * distance

            if cur > 100:
                passed_by_zero += 1
            elif cur < 0 and initial != 0:
                passed_by_zero += 1

            cur = cur % 100
            if cur == 0:
                zeroes_seen += 1

            print(
                f"Move {line.strip()} to {cur}. Pass={passed_by_zero} Ended={zeroes_seen}"
            )

    print(f"Part One: The number of zeroes seen is {zeroes_seen}")
    print(f"Part Two: The number of times passed by zero is {passed_by_zero}")
    print(
        f"Part Two: So passed by and stopped on zero = {zeroes_seen + passed_by_zero}"
    )


if __name__ == "__main__":
    part_one()
