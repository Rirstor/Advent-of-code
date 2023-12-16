import numpy as np
import sys

sys.setrecursionlimit(4000)
puzzle = [[i for i in l.split()[0]] for l in open("day16/input")]

directions = dict(N=(-1, 0), S=(1, 0), W=(0, -1), E=(0, 1))

count = 0


def propagate(point, d, output=None):
    global count
    count += 1
    print(count)
    if output is None:
        output = dict()
    offset_dir = directions[d]
    next_point = (point[0] + offset_dir[0], point[1] + offset_dir[1])

    if any([(i < 0) or (i > len(puzzle) - 1) for i in next_point]):
        return None
    # npo = tuple(next_point.tolist())

    if next_point not in output:
        output[next_point] = [d]
    else:
        d_seen = output[next_point]
        if d not in d_seen:
            d_seen.append(d)
        else:
            return None

    sn = puzzle[next_point[0]][next_point[1]]
    if sn == ".":
        propagate(next_point, d, output)

    elif sn == "/":
        if d == "E":
            propagate(next_point, "N", output)
        elif d == "W":
            propagate(next_point, "S", output)
        elif d == "N":
            propagate(next_point, "E", output)
        elif d == "S":
            propagate(next_point, "W", output)
    elif sn == "\\":
        if d == "E":
            propagate(next_point, "S", output)
        elif d == "W":
            propagate(next_point, "N", output)
        elif d == "N":
            propagate(next_point, "W", output)
        elif d == "S":
            propagate(next_point, "E", output)

    elif sn == "-":
        if d in ["N", "S"]:
            for nex_d in ["W", "E"]:
                propagate(next_point, nex_d, output)
        else:
            propagate(next_point, d, output)

    elif sn == "|":
        if d in ["W", "E"]:
            for nex_d in ["N", "S"]:
                propagate(next_point, nex_d, output)
        else:
            propagate(next_point, d, output)


output = dict()
res = propagate((0, -1), "E", output)
print(len(set(output.keys())))
