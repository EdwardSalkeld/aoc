import scipy


class Machine:
    def __init__(
        self,
        target_state: int,
        operations: list[int],
        joltage_target: list[int],
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
    # so what we want is the joltage target
    target = machine.joltage_target

    # we can unpack the operations from binary
    arr_opts: list[list[int]] = []
    for i in range(len(target)):
        arr_opt: list[int] = []
        for opt in machine.operations:
            if opt & 1 << i:
                arr_opt.append(1)
            else:
                arr_opt.append(0)
        arr_opts.append(arr_opt)

    # and we want to minimise the attempts
    equality = [1] * len(machine.operations)

    # build an optimiser. integrality=1 means we want ints back
    optimiser = scipy.optimize.linprog(
        c=equality, integrality=1, A_eq=arr_opts, b_eq=target
    )
    if optimiser.status == 0:
        return round(optimiser.fun)


def expand_input(raw_input: list[str]) -> list[Machine]:
    machines = []
    for line in raw_input:
        parts = line.split(" ")
        operations: list[int] = []
        joltage_operations: list[int] = []
        target: int = 0
        joltage = ""
        joltage_target: list[int] = []
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
                joltage_operation: int = 0
                for op in ops:
                    operation |= 1 << int(op)
                    joltage_operation += 10 ** (3 * int(op))
                operations.append(operation)
                joltage_operations.append(joltage_operation)

            elif part.startswith("{") and part.endswith("}"):
                joltage = part[1:-1]
                joltage_target = [int(j) for j in joltage.split(",")]

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
