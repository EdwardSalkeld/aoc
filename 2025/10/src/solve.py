class Machine:
    def __init__(
        self,
        target_state: int,
        operations: list[int],
        joltage_target: int,
        joltage_operations: list[int],
    ):
        self.target_state = target_state
        self.operations = operations
        self.joltage_target = joltage_target
        self.joltage_operations = joltage_operations


def solve(part: int = 1) -> int:
    raw_input = read_input()
    machines = expand_input(raw_input)
    if part == 1:
        answer = 0
        for machine in machines:
            answer += solve_machine(machine)
        return answer
    if part == 2:
        answer = 0
        for ix, machine in enumerate(machines):
            print(f"Solving machine {ix + 1}/{len(machines)}")
            answer += solve_joltage(machine)
        return answer
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
            state_stack = list(state[1])
            state_stack.append(operation)
            new_state = (new_state_val, state_stack)
            if new_state_val == target:
                print(
                    f"Found target {target:b} at depth {depth} with operations {state_stack}"
                )
                return depth
            new_states.append(new_state)
    return try_operations(target, list(new_states), operations, depth + 1)


def solve_joltage(machine: Machine) -> int:
    return try_joltage_operations(
        machine.joltage_target, [(0, [])], machine.joltage_operations, 1
    )


def try_joltage_operations(
    target: int, states: list[StateTrace], operations: list[int], depth: int
) -> int:
    new_states = {}
    print(f"Depth {depth}, States to explore: {len(states)}")
    print(
        f"difference between target and min state = {target - min(s[0] for s in states)}"
    )
    for state in states:
        for operation in operations:
            new_state_val = state[0] + operation
            state_stack = list(state[1])
            state_stack.append(operation)
            # print(
            #     f"Depth={depth}, Current={state[0]}, Op={operation}, New={new_state_val}"
            # )
            new_state = (new_state_val, state_stack)
            if new_state_val == target:
                print(
                    f"Found target {target:b} at depth {depth} with operations {state_stack}"
                )
                return depth
            if new_state_val < target:
                new_states[new_state_val] = new_state
    return try_joltage_operations(
        target, list(new_states.items()), operations, depth + 1
    )


def expand_input(raw_input: list[str]) -> list[Machine]:
    machines = []
    for line in raw_input:
        parts = line.split(" ")
        operations = []
        joltage_operations = []
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
                joltage_operation = 0
                for op in ops:
                    operation |= 1 << int(op)
                    joltage_operation += 10 ** (3 * int(op))
                operations.append(operation)
                joltage_operations.append(joltage_operation)

            elif part.startswith("{") and part.endswith("}"):
                joltage = part[1:-1]
                joltage_target = 0
                for ix, counter_str in enumerate(joltage.split(",")):
                    counter = int(counter_str)

                    if counter > 999:
                        raise ValueError("Counter too large")
                    # print(
                    #     f"Adding 3*{ix} ** 10 * {counter} = {10 ** (3 * ix) * counter}"
                    # )
                    joltage_target += 10 ** (3 * ix) * counter

        machine = Machine(target, operations, joltage_target, joltage_operations)
        # print("\n")
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
