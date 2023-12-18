from itertools import chain
import shapely as sh

plan = [l.strip().split() for l in open("day18/input")]
movements = dict(U=(-1, 0), D=(1, 0), R=(0, 1), L=(0, -1))


def coords(point, data):
    m, d = data[0], int(data[1])
    offset = movements[m]
    np = (point[0] + d * offset[0], point[1] + d * offset[1])
    return np


def shoelace(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def pick(perimeter, area):
    return int(area + 1 - perimeter // 2)


def solve(plan):
    result = [(0, 0)]
    for d in plan:
        np = coords(result[-1], d)
        result.append(np)
    area = abs(
        sum((shoelace(result[i], result[i + 1])) for i in range(len(result) - 1)) + shoelace(result[-1], result[0])) / 2
    perimeter = sum((manhattan(result[i], result[i + 1])) for i in range(len(result) - 1))
    print(pick(perimeter, area) + perimeter)


# part 1
solve(plan)

# part 2
assign = {'0': "R", '1': "D", '2': "L", '3': "U"}
new_plan = [(assign[elt[-1][-2]], int(elt[-1][2:-2], 16)) for elt in plan]
solve(new_plan)
