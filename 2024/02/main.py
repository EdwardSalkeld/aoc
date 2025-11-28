# read the file into two lists
list1: list[int] = []
list2: list[int] = []
with open("input", "r") as f:
    lines = f.readlines()
    for line in lines:
        n1, n2 = line.strip().split()
        list1.append(int(n1))
        list2.append(int(n2))


# calculate appearences of number in list2
appearences: dict[int, int] = {}
for n in list2:
    if n in appearences:
        appearences[n] += 1
    else:
        appearences[n] = 1


# iterate and multiply value by appearences
total = 0
for n in list1:
    value = n * appearences.get(n, 0)
    print(f"adding {n} * {appearences.get(n, 0)} = {value}")
    total += value

print(f"Total similarity score: {total}")
