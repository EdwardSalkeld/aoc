class Machine:
    def __init__(self, target_state: int, operations: list[int], joltages: str):
        self.target_state = target_state
        self.operations = operations
        self.joltages = joltages


def solve(part: int = 1) -> int:
    raw_input = read_input()
    machines = expand_input(raw_input)
    if part == 1:
        answer = 0
        for machine in machines:
            answer += solve_machine(machine)
        return answer
    answer = 0
    return 0


def solve_machine(machine: Machine) -> int:
    return try_operations(machine.target_state, [(0, [])], machine.operations, 1)


type StateTrace = tuple[int, list[int]]


def try_operations(
    target: int, states: list[StateTrace], operations: list[int], depth: int
) -> int:
    new_states = []
    for state in states:
        for operation in operations:
            new_state_val = state[0] ^ operation
            state_stack = state[1]
            state_stack.append(operation)
            new_state = (new_state_val, state_stack)
            if new_state_val == target:
                print(
                    f"Found target {target:b} at depth {depth} with operations {state_stack}"
                )
                return depth
            new_states.append(new_state)
    return try_operations(target, list(new_states), operations, depth + 1)


def expand_input(raw_input: list[str]) -> list[Machine]:
    machines = []
    for line in raw_input:
        parts = line.split(" ")
        operations = []
        joltage = ""
        for part in parts:
            if part.startswith("[") and part.endswith("]"):
                lights = part[1:-1]
                target = 0
                for ix, light in enumerate(list(lights)):
                    if light == "#":
                        target |= 1 << ix
            elif part.startswith("(") and part.endswith(")"):
                ops = part[1:-1].split(",")
                operation = 0
                for op in ops:
                    operation |= 1 << int(op)
                operations.append(operation)
            elif part.startswith("{") and part.endswith("}"):
                joltage = part[1:-1]
        machine = Machine(target, operations, joltage)
        machines.append(machine)
    return machines


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
