from functools import reduce

data = [line.strip() for line in open("input")]

datastored = dict()

for id_row in range(len(data)):
    for id_col in range(len(data[0])):
        value = data[id_row][id_col]
        if value not in datastored:
            datastored[value] = set()
        datastored[value].add((id_row, id_col))
wholeset = reduce(set.union, datastored.values())


def f(pos, elts=()):
    x, y = pos[0], pos[1]
    value = int(data[x][y])
    if value == 9:
        elts.append((x, y))
        return elts
    for xoff, yoff in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        xnew = x + xoff
        ynew = y + yoff
        if (xnew, ynew) in wholeset:
            newvalue = int(data[xnew][ynew])
            if newvalue - value == 1:
                f((xnew, ynew), elts)
    return elts


part1 = [set(f(pos, list())) for pos in datastored["0"]]
print(sum(len(elt) for elt in part1))

part2 = [f(pos, list()) for pos in datastored["0"]]
print(sum(len(elt) for elt in part2))
