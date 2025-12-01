def part_one():
    cur = 50
    zeroes_seen = 0

    with open("input") as f:
        for line in f:
            direction = -1 if line[0] == "L" else 1
            distance = int(line[1:].strip())
            cur += direction * distance
            cur_num = cur % 100
            if cur_num == 0:
                zeroes_seen += 1

    print(f"The number of zeroes seen is {zeroes_seen}")


if __name__ == "__main__":
    part_one()
