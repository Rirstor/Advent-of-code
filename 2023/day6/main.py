import re
import numpy as np


def dist(time):
    return [i * (time - i) for i in range(time)]


times, distance = [list(map(int, re.findall("\d+", l))) for l in open("day6/data.txt")]

results = np.prod(list(sum([elt > d for elt in dist(t)]) for t, d in zip(times, distance)))
print(results)

times2, distance2 = [int("".join(re.findall("\d+", l))) for l in open("day6/data.txt")]

a = -1
b = times2
c = -distance2

descri = b ** 2 - 4 * a * c

x1 = (-times2 - np.sqrt(descri)) / 2 * a
x2 = (-times2 + np.sqrt(descri)) / 2 * a

x1 = int(np.floor(x1))
x2 = int(np.ceil(x2))
print(x1 - x2 + 1)
