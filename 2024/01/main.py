# read the file into two lists
list1: list[int] = []
list2: list[int] = []
with open("input", "r") as f:
    lines = f.readlines()
    for line in lines:
        n1, n2 = line.strip().split()
        list1.append(int(n1))
        list2.append(int(n2))

# sort 'em
list1 = sorted(list1)
list2 = sorted(list2)

# iterate and get abs diff
total = 0
for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    total += diff

print(f"Total absolute difference: {total}")
