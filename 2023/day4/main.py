import re

cards = [line.split(":")[1].replace("\n", "").split("|") for line in open("day4/data.txt")]

matches = [[elt.strip().split() for elt in line] for line in cards]

result = [sum([side1 in a for side1 in b]) for a, b in matches]
print(sum(int(2 ** (elt - 1)) for elt in result))


def part2(idx):
    output = 0
    if result[idx] == 0:
        return output + 1
    else:
        return output + 1 + sum(part2(idx + idx_range) for idx_range in range(1, result[idx] + 1))


print(sum(part2(idx) for idx in range(len(result))))
