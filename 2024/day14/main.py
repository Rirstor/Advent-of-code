import re
from math import prod
from statistics import variance

inputs = [line.strip() for line in open("input")]

robots = [list(map(int, *re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", elt))) for elt in inputs]

# part 1

nbtiles = 101
height = 103
nb_seconds = 100


def f(posx, posy, vx, vy, t):
    xnew = (posx + t * vx) % nbtiles
    ynew = (posy + t * vy) % height
    return (xnew, ynew)


def count_quadrant(xmin, xmax, ymin, ymax, positions):
    elts = [i for i in positions if xmin <= i[0] < xmax and ymin <= i[1] < ymax]
    return len(elts)


positions = [f(*elt, t=nb_seconds) for elt in robots]
part1 = list()
for xmin, xmax in ((0, nbtiles // 2), (nbtiles // 2 + 1, nbtiles)):
    for ymin, ymax in ((0, height // 2), (height // 2 + 1, height)):
        part1.append(count_quadrant(xmin, xmax, ymin, ymax, positions))

print(prod(part1))

# part2
nb_quadrants = list()
variances = list()
for id_sec in range(10000):
    positions_each_sec = [f(*elt, t=id_sec) for elt in robots]
    variances.append(variance(elt[0] for elt in positions_each_sec) * variance(elt[1] for elt in positions_each_sec))
    res = list()
    for xmin, xmax in ((0, nbtiles // 2), (nbtiles // 2 + 1, nbtiles)):
        for ymin, ymax in ((0, height // 2), (height // 2 + 1, height)):
            res.append(count_quadrant(xmin, xmax, ymin, ymax, positions_each_sec))

    nb_quadrants.append(prod(res))
print([i for i in range(len(variances)) if variances[i] == min(variances)])
