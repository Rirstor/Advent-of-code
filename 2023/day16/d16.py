import sys

sys.setrecursionlimit(5000)
puzzle = [[i for i in l.split()[0]] for l in open("day16/input")]

directions = dict(N=(-1, 0), S=(1, 0), W=(0, -1), E=(0, 1))


def propagate(point, d, output_f=None):
    if output_f is None:
        output_f = dict()
    offset_dir = directions[d]
    next_point = (point[0] + offset_dir[0], point[1] + offset_dir[1])

    if any([(i < 0) or (i > len(puzzle) - 1) for i in next_point]):
        return None

    if next_point not in output_f:
        output_f[next_point] = [d]
    else:
        d_seen = output_f[next_point]
        if d not in d_seen:
            d_seen.append(d)
        else:
            return None

    sn = puzzle[next_point[0]][next_point[1]]
    if sn == ".":
        propagate(next_point, d, output_f)

    elif sn == "/":
        if d == "E":
            propagate(next_point, "N", output_f)
        elif d == "W":
            propagate(next_point, "S", output_f)
        elif d == "N":
            propagate(next_point, "E", output_f)
        elif d == "S":
            propagate(next_point, "W", output_f)
    elif sn == "\\":
        if d == "E":
            propagate(next_point, "S", output_f)
        elif d == "W":
            propagate(next_point, "N", output_f)
        elif d == "N":
            propagate(next_point, "W", output_f)
        elif d == "S":
            propagate(next_point, "E", output_f)

    elif sn == "-":
        if d in ["N", "S"]:
            for nex_d in ["W", "E"]:
                propagate(next_point, nex_d, output_f)
        else:
            propagate(next_point, d, output_f)

    elif sn == "|":
        if d in ["W", "E"]:
            for nex_d in ["N", "S"]:
                propagate(next_point, nex_d, output_f)
        else:
            propagate(next_point, d, output_f)


output = dict()
propagate((0, -1), "E", output)
# part 1
print(len(set(output.keys())))

# part 2

res = 0
pr1 = [(-1, i) for i in range(len(puzzle))]
pr2 = [(len(puzzle), i) for i in range(len(puzzle))]

pc1 = [(i, -1) for i in range(len(puzzle))]
pc2 = [(i, len(puzzle)) for i in range(len(puzzle))]
res = 0
for points, d in zip([pr1, pr2, pc1, pc2], ["S", "N", "E", "W"]):

    for p in points:
        output = dict()
        propagate(p, d, output)
        r = len(set(output.keys()))
        if r > res:
            res = r
print(res)
