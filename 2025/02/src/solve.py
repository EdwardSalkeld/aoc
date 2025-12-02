def solve(part: int = 1) -> int:
    invalid_ids = []
    raw_input = read_input()
    unpacked_input = expand_input(raw_input)
    for item in unpacked_input:
        if part == 1 and not check_item(item):
            invalid_ids.append(item)
        elif part == 2 and not check_item_part2(item):
            invalid_ids.append(item)
    invalid_id_sum = sum(invalid_ids)
    return invalid_id_sum


def main() -> None:
    invalid_id_sum = solve()
    print(f"Sum of invalid IDs: {invalid_id_sum}")
    invalid_id_sum_part2 = solve(part=2)
    print(f"Sum of invalid IDs (part 2): {invalid_id_sum_part2}")


def read_input() -> str:
    with open("./input", "r") as f:
        return f.readline()


def expand_input(raw_input: str) -> list[int]:
    ids = []
    elements = raw_input.strip().split(",")
    for element in elements:
        if "-" in element:
            start, end = map(int, element.split("-"))
            ids.extend(range(start, end + 1))
        else:
            ids.append(int(element))
    return ids


def check_item(item_id: int) -> bool:
    item = str(item_id)
    # anything with no repeated chars is valid.
    if len(set(item)) == len(item):
        return True

    if int(len(item)) % 2 == 1:
        return True
    sequence_lenth = int(len(item) / 2)
    if item[:sequence_lenth] == item[sequence_lenth : sequence_lenth * 2]:
        return False
    return True


def check_item_part2(item_id: int) -> bool:
    item = str(item_id)
    all_char_count = len(set(item))
    # anything with no repeated chars is valid.
    if all_char_count == len(item):
        return True

    max_length_sequence = len(item) / 2
    for sequence_length in range(1, int(max_length_sequence) + 1):
        if len(item) % sequence_length != 0:
            continue  # can't make the whole thing with a sequence this length

        sequences_to_check = len(item) / sequence_length
        sequences = set()
        for i in range(int(sequences_to_check)):
            sequence = item[i * sequence_length : (i + 1) * sequence_length]
            sequences.add(sequence)
        if len(sequences) == 1:
            return False
    return True


if __name__ == "__main__":
    main()
