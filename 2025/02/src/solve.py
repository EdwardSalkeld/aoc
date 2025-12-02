def solve() -> int:
    invalid_ids = []
    raw_input = read_input()
    unpacked_input = expand_input(raw_input)
    for item in unpacked_input:
        if not check_item(item):
            invalid_ids.append(item)
    invalid_id_sum = sum(invalid_ids)
    return invalid_id_sum


def main() -> None:
    invalid_id_sum = solve()
    print(f"Sum of invalid IDs: {invalid_id_sum}")


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
        print(
            f"DBG: {item} is invalid, repeated sequence {item[:sequence_lenth]} found"
        )
        return False
    # max_length_sequence = len(item) / 2
    # for sequence_length in range(1, int(max_length_sequence) + 1):
    #     for start in range(len(item) - 2 * sequence_length + 1):
    #         sequence = item[start : start + sequence_length]
    #         next_sequence = item[start + sequence_length : start + 2 * sequence_length]
    #         # print(f"DBG: checking {item}. S1[{sequence}] S2[{next_sequence}]")
    #         if sequence == next_sequence:
    #             if sequence_length > 1:
    #                 print(f"DBG: {item} is invalid, repeated sequence {sequence} found")
    #             return False
    return True


if __name__ == "__main__":
    main()
