import numpy as np

space = np.array([[elt for elt in line.split()[0]] for line in open("day11/input.txt")])
points = np.argwhere(space == "#")
is_empty = space == "."
l = len(space)
rows = [i for i in range(l) if is_empty.sum(1)[i] == len(space)]
columns = [i for i in range(l) if is_empty.sum(0)[i] == len(space)]


def dist(xA, yA, xB, yB, rows, columns):
    dist = np.abs(xA - xB) + np.abs(yA - yB)
    if dist > 0:
        dist += sum([min(xA, xB) < elt < max(xA, xB) for elt in rows]) *(1000000-1)
        dist += sum([min(yA, yB) < elt < max(yA, yB) for elt in columns]) *(1000000-1)
    return dist


output = 0
for i in range(len(points)):
    for j in range(i, len(points)):
        output += dist(*points[i], *points[j], rows, columns)
print(output)