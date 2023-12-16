import numpy as np
import sys

sys.setrecursionlimit(2166)
puzzle = np.array([[i for i in l.split()[0]] for l in open("day16/input")])

directions = dict(N=(-1, 0), S=(1, 0), W=(0, -1), E=(0, 1))


def propagate(point, d, puzzle, output=None):
    if output is None:
        output = list()
    next_point = point + np.array(directions[d])

    if any([(i < 0) or (i > len(puzzle) - 1) for i in next_point]):
        return None
    npo = tuple(next_point.tolist())
    if [npo, d] not in output:
        output.append([npo, d])
    else:
        return None
    sn = puzzle[next_point[0], next_point[1]]
    if sn == ".":
        propagate(next_point, d, puzzle, output)

    elif sn == "/":
        if d == "E":
            propagate(next_point, "N", puzzle, output)
        elif d == "W":
            propagate(next_point, "S", puzzle, output)
        elif d == "N":
            propagate(next_point, "E", puzzle, output)
        elif d == "S":
            propagate(next_point, "W", puzzle, output)
    elif sn == "\\":
        if d == "E":
            propagate(next_point, "S", puzzle, output)
        elif d == "W":
            propagate(next_point, "N", puzzle, output)
        elif d == "N":
            propagate(next_point, "W", puzzle, output)
        elif d == "S":
            propagate(next_point, "E", puzzle, output)

    elif sn == "-":
        if d in ["N", "S"]:
            for nex_d in ["W", "E"]:
                propagate(next_point, nex_d, puzzle, output)
        else:
            propagate(next_point, d, puzzle, output)

    elif sn == "|":
        if d in ["W", "E"]:
            for nex_d in ["N", "S"]:
                propagate(next_point, nex_d, puzzle, output)
        else:
            propagate(next_point, d, puzzle, output)


output = list()
res = propagate(np.array([0, -1]), "E", puzzle, output)
print(len(set(i[0] for i in output)))
