import re
from math import prod

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

from re import findall
data = open("input").read()
W, H = 101, 103

robots = [[int(n) for n in findall(r"(-?\d+)", item)] for item in data.split("\n")]

import re

w, h = 101, 103
bots = [[*map(int, re.findall(r'-?\d+',l))]
                   for l in open('input')]

def danger(t):
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * t) % w
        y = (y + dy * t) % h

        a += x > w//2 and y > h//2
        b += x > w//2 and y < h//2
        c += x < w//2 and y > h//2
        d += x < w//2 and y < h//2

    return a * b * c * d

print(danger(100))
print(min(range(10_000), key=danger))


# part2
nb_quadrants = list()
for id_sec in range(10000):
    positions_each_sec = [f(*elt, t=id_sec) for elt in robots]
    res = list()
    for xmin, xmax in ((0, nbtiles // 2), (nbtiles // 2 + 1, nbtiles)):
        for ymin, ymax in ((0, height // 2), (height // 2 + 1, height)):
            res.append(count_quadrant(xmin, xmax, ymin, ymax, positions_each_sec))
    nb_quadrants.append(prod(res))
print(1)
