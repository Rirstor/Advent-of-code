from itertools import combinations
from functools import reduce

inputs = [line.strip() for line in open("day08/input")]

# part1

data = dict()

for id_row in range(len(inputs)):
    for id_col in range(len(inputs[0])):
        value = inputs[id_row][id_col]
        if value not in data:
            data[value] = set()
        data[value].add((id_row, id_col))
wholeset = reduce(set.union, data.values())


def f(pos1, pos2, result=set()):
    vect = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    newpos2 = (pos2[0] + vect[0], pos2[1] + vect[1])
    newpos1 = (pos1[0] - vect[0], pos1[1] - vect[1])

    for pos in (newpos1, newpos2):
        if pos in wholeset:
            result.add(pos)


part1 = set()
[f(elt[0], elt[1], result=part1) for key in (set(data.keys()) - {"."}) for elt in
 combinations(data[key], r=2)]

print(len(part1))


# part2

def g(pos1, pos2, result=set()):
    vect = (pos2[0] - pos1[0], pos2[1] - pos1[1])

    newpos2 = tuple((pos2[0] + i * vect[0], pos2[1] + i * vect[1]) for i in range(len(inputs)))
    newpos1 = tuple((pos1[0] - i * vect[0], pos1[1] - i * vect[1]) for i in range(len(inputs)))

    for pos in (newpos1 + newpos2):
        if pos in wholeset:
            result.add(pos)


part2 = set()
[g(elt[0], elt[1], result=part2) for key in (set(data.keys()) - {"."}) for elt in
 combinations(data[key], r=2)]

print(len(part2))
